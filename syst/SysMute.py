"""
This per-server warn system is designed to be as storage efficient
as possible; it aims to minimize the number of records stored per
user, allowing large number of records to be stored in a small amount
of space :)
"""

from __future__ import annotations

import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING, IndexModel

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = 'core'
COL_NAME = 'roles'

#

def toInt(snowflake: str) -> int:
   return snowflake

#

class Mute:
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

   async def ApplyHardMute_(self, user, mute_role) -> None:
      uid_ = toInt(user.id)
      gid_ = toInt(user.guild.id)
      roles = [
         role.id for role in user.roles
         if role.name != '@everyone' and role.id != mute_role.id
      ]

      result = await self._col.find_one_and_update(
         {
            '_id': uid_,
            'g.id': gid_
         },
         {
            '$set': {'g.$.r': roles}
         }
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
                  'r': roles
               }]
            })

         else:
            await self._col.update_one(
               {'_id': uid_},
               {'$push': { 'g': {
                  'id': gid_,
                  'r': roles
               }}},
            )

      await user.edit(roles = [mute_role])

   async def ApplyMute(self, user, mute_role) -> None:
      await user.add_roles(mute_role)

   async def RemoveHardMute_(self, user, mute_role) -> bool:
      uid_ = toInt(user.id)
      gid_ = toInt(user.guild.id)

      doc = await self._col.find_one(
         {
            '_id': uid_,
            'g.id': gid_
         },
         projection = {'g.$': 1}
      )

      if doc is None:
         return False

      role_ids = doc['g'][0].get('r', [])
      roles = [r for rid in role_ids if (r := user.guild.get_role(rid))]

      await user.edit(roles = roles)

      await self._col.update_one(
         {'_id': uid_},
         {'$pull': { 'g': {
            'id': gid_,
         }}},
      )
      await self._col.delete_one(
         {
            '_id': uid_,
            'g': []
         }
      )

      return True

   async def RemoveMute_(self, user, mute_role) -> None:
      await user.remove_roles(mute_role)

   async def IsMuted_(self, user_id: int, guild_id: int) -> bool:
      doc = await self._col.find_one(
         {
            '_id': toInt(user_id),
            'g.id': toInt(guild_id)
         },
         projection = {'_id': 1}
      )
      return doc is not None