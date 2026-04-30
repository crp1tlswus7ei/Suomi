import os
from discord.ext import commands
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
shot = MongoClient(MONGO_URI)
db = shot['core']
w_coll = db['prefix']
DEFAULT_PREFIX = '!'
AUX_PREFIX = 'core'

async def GetPrefix_(bot, message):
   if not message.guild:
      commands.when_mentioned_or(
         DEFAULT_PREFIX, AUX_PREFIX
      )(
         bot, message
      )

   custom_ = None
   prefixes = [DEFAULT_PREFIX, AUX_PREFIX]

   data = w_coll.find_one(
      {
         '_id': message.guild.id
      }
   )

   if data:
      custom_ = data.get('prefix')

   if custom_:
      prefixes.insert(0, custom_)

   return commands.when_mentioned_or(*prefixes)(bot, message)

async def GetActualPrefix_(guild_id: int):
   prefix = w_coll.find_one(
      {
         '_id': guild_id
      }
   )
   return prefix['prefix']

async def UpdatePrefix_(ctx, new_prefix):
   w_coll.update_one(
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
   w_coll.update_one(
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