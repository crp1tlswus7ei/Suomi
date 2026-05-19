"""
This per-server level system is designed to be as storage efficient
as possible; it aims to minimize the number of records stored per
user, allowing large number of records to be stored in a small amount
of space
"""

from __future__ import annotations

import os
import time
import random
import discord
from typing import Optional
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING, IndexModel, ReturnDocument

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = 'core'
COL_NAME = 'levels'
#
XP_MIN = 15
XP_MAX = 25
XP_COOLDOWN_SEC = 60

#

def xpForLevel(level: int) -> int:
   return 5 * (level ** 2) + 50 * level + 100

def nowMinutes() -> int:
   return int(time.time() // 60)

def toInt(snowflake: int) -> int:
   return snowflake

#

class Level:
   def __init__(self, mongo_uri: str = MONGO_URI, db_name: str = DB_NAME):
      self._client = AsyncIOMotorClient(mongo_uri)
      self._col = self._client[db_name][COL_NAME]

   async def setup(self) -> None:
      await self._col.create_indexes([
         IndexModel(
            [('g.id', ASCENDING)],
            name = 'guild_id'
         ),
      ])

   async def on_message(self, message: discord.Message) -> Optional[tuple[int, int]]:
      if message.guild is None:
         return None

      uid_ = toInt(message.author.id)
      gid_ = toInt(message.guild.id)
      now_min = nowMinutes()
      cooldown = XP_COOLDOWN_SEC // 60 or 1
      xp_gain = random.randint(XP_MIN, XP_MAX)

      result = await self._col.find_one_and_update(
         {
            '_id': uid_,
            'g': {
               '$elemMatch': {
                  'id': gid_,
                  'lm': {'$lte': now_min - cooldown}
               }
            }
         },
         {
            '$inc': {'g.$.xp': xp_gain},
            '$set': {'g.$.lm': now_min}
         },
         return_document = ReturnDocument.AFTER
      )

      if result is None:
         user_exists = await self._col.find_one(
            {'_id': uid_},
            projection = {'_id': 1}
         )

         if user_exists is None:
            await self._col.insert_one({
               '_id': uid_,
               'g': [{
                  'id': gid_,
                  'xp': xp_gain,
                  'lv': 0,
                  'lm': now_min
               }]
            })

         else:
            guild_entry = await self._col.find_one(
               {'_id': uid_, 'g.id': gid_},
               projection = {'g.$': 1}
            )

            if guild_entry is None:
               await self._col.update_one(
                  {'_id': uid_},
                  {'$push': {'g': {
                     'id': gid_,
                     'xp': xp_gain,
                     'lv': 0,
                     'lm': now_min
                  }}},
               )
            return None

         result = await self._col.find_one(
            {'_id': uid_, 'g.id': gid_},
            projection = {'g.$': 1}
         )

      entry = next(e for e in result['g'] if e['id'] == gid_)
      current_xp = entry['xp']
      current_lv = entry['lv']
      new_lv  = current_lv

      while current_xp >= xpForLevel(new_lv + 1):
         new_lv += 1

      if new_lv > current_lv:
         await self._col.update_one(
            {'_id': uid_, 'g.id': gid_},
            {'$set': {'g.$.lv': new_lv}}
         )
         return new_lv, current_lv

      return None

   async def GetUserLevel(self, user_id: int, guild_id: int) -> Optional[dict]:
      doc = await self._col.find_one(
         {'_id': toInt(user_id), 'g.id': toInt(guild_id)},
         projection = {'g.$': 1}
      )
      if doc is None:
         return None

      entry = doc['g'][0]
      return {'xp': entry['xp'], 'lv': entry['lv']}

   async def GetLeaderboard(self, guild_id: int, limit: int = 10) -> list[dict]:
      gid_ = toInt(guild_id)

      pipeline = [
         {'$match':   {'g.id': gid_}},
         {'$unwind':  '$g'},
         {'$match':   {'g.id': gid_}},
         {'$sort':    {'g.xp': -1}},
         {'$limit':   limit},
         {'$project': {'_id': 1, 'xp': '$g.xp', 'lv': '$g.lv'}},
      ]

      return [
         {'user_id': doc['_id'], 'xp': doc['xp'], 'lv': doc['lv']}
         async for doc in self._col.aggregate(pipeline)
      ]