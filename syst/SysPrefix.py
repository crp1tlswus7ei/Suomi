import os
from discord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
shot = AsyncIOMotorClient(MONGO_URI)
db = shot['core']
w_coll = db['prefix']
DEFAULT_PREFIX = '$'
AUX_PREFIX = 'su'

async def GetPrefix_(bot, message):
   if not message.guild:
      return commands.when_mentioned_or(
         DEFAULT_PREFIX, AUX_PREFIX
      )(
         bot, message
      )

   prefixes = [DEFAULT_PREFIX, AUX_PREFIX]

   data = await w_coll.find_one(
      {
         '_id': message.guild.id
      }
   )

   if data:
      prefixes.insert(0, data['prefix'])

   return commands.when_mentioned_or(*prefixes)(bot, message)

async def GetActualPrefix_(guild_id: int):
   data = await w_coll.find_one(
      {
         '_id': guild_id
      }
   )
   return data['prefix'] if data else DEFAULT_PREFIX

async def UpdatePrefix_(ctx, new_prefix):
   await w_coll.update_one(
      {
         '_id': ctx.guild.id
      },
      {
         '$set': {
            'prefix': new_prefix
         }
      },
      upsert = True
   )

async def ResetPrefix_(ctx):
   await w_coll.update_one(
      {
         '_id': ctx.guild.id
      },
      {
         '$set': {
            'prefix': DEFAULT_PREFIX
         }
      },
      upsert = True
   )

async def ResetGuildPrefix_(guild_id: int):
   await w_coll.update_one(
      {
         '_id': guild_id
      },
      {
         '$set': {
            'prefix': DEFAULT_PREFIX
         }
      },
      upsert = True
   )

async def DeletePrefix_(guild_id: int):
   await w_coll.delete_one(
      {
         '_id': guild_id
      }
   )