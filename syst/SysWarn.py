"""
This per-server warn system is designed to be as storage efficient
as possible; it aims to minimize the number of records stored per
user, allowing large number of records to be stored in a small amount
of space :O
"""

from __future__ import annotations

import os
from dotenv import load_dotenv
from datetime import datetime, timezone
from pymongo import ASCENDING, IndexModel
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = 'core'
COL_NAME = 'warns'

#

def toInt(snowflake: int) -> int:
   return snowflake

#

class Warn:
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

   #

   async def GetWarns_(self, user_id: int, guild_id: int) -> list[str]:
      doc = await self._col.find_one(
         {
            '_id': toInt(user_id),
            'g.id': toInt(guild_id)
         },
         projection = {'g.$': 1}
      )

      if doc is None:
         return []

      return doc['g'][0]['w']

   async def GetAllWarns_(self, user_id: int) -> dict[int, list[str]]:
      doc = await self._col.find_one(
         {'_id': toInt(user_id)},
         projection = {'g': 1}
      )

      if doc is None:
         return {}

      return {
         entry['id']: entry['w']
         for entry in doc.get('g', [])
         if entry.get('w')
      }

   async def AddWarns_(self, user_id: int, guild_id: int, author_id: int, reason: str) -> int:
      uid_ = toInt(user_id)
      gid_ = toInt(guild_id)
      entry = {
         'r': reason,
         'd': datetime.now(timezone.utc).timestamp(),
         'a': toInt(author_id)
      }

      result = await self._col.find_one_and_update(
         {
            '_id': uid_,
            'g.id': gid_
         },
         {
            '$push': {'g.$.w': entry}
         },
         return_document = True
      )

      if result is not None:
         e = next(e for e in result['g'] if e['id'] == gid_)
         return len(e['w'])

      user_exists = await self._col.find_one(
         {'_id': uid_},
         projection = {'_id': 1}
      )

      if user_exists is None:
         await self._col.insert_one(
            {
               '_id': uid_,
               'g': [{
                  'id': gid_,
                  'w': [entry]
               }]
            })
      else:
         await self._col.update_one(
            {'_id': uid_},
            {'$push': { 'g': {
               'id': gid_,
               'w': [entry]
            }}},
         )

      return 1

   async def RemoveWarn_(self, user_id: int, guild_id: int, index: int) -> bool:
      warns = await self.GetWarns_(user_id, guild_id)

      if not (0 <= index < len(warns)):
         return False

      del warns[index]
      uid_ = toInt(user_id)
      gid_ = toInt(guild_id)

      if not warns:
         await self._col.update_one(
            {'_id': uid_},
            {'$pull': { 'g': {
               'id': gid_
            }}},
         )
         await self._col.delete_one(
            {
               '_id': uid_,
               'g': []
            }
         )
      else:
         await self._col.update_one(
            {
               '_id': uid_,
               'g.id': gid_
            },
            {
               '$set': {'g.$.w': warns}
            }
         )

      return True

   async def ClearWarns_(self, user_id: int, guild_id: int) -> None:
      uid_ = toInt(user_id)
      gid_ = toInt(guild_id)

      await self._col.update_one(
         {'_id': uid_},
         {'$pull': {'g': {
            'id': gid_
         }}},
      )
      await self._col.delete_one(
         {
            '_id': uid_,
            'g': []
         }
      )