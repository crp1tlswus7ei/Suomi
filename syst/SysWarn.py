"""
Please ignore the weak warnings about self parameter not being used
since these functions are imported into command class and rely on self;
without it, they will not work, and there is no error handling for this.
"""

import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
shot = MongoClient(MONGO_URI)
db = shot['core']
w_coll = db['warns']

def GetWarns_(self, guild_id, user_id):
   userData = w_coll.find_one(
      {
         'guild_id': guild_id,
         'user_id': user_id
      }
   )
   return userData['warnings'] if userData else []

def AddWarns_(self, guild_id, user_id, reason):
   warns = self.GetWarns_(guild_id, user_id)
   warns.append(reason)

   w_coll.update_one(
      {
         'guild_id': guild_id,
         'user_id': user_id
      },
      {
         '$set': {
            'warnings': warns
         }
      },
      upsert = True
   )

   return len(warns)

def ClearWarns_(self, guild_id, user_id):
   w_coll.update_one(
      {
         'guild_id': guild_id,
         'user_id': user_id
      },
      {
         '$set': {
            'warnings': []
         }
      }
   )

def RemoveWarn_(self, guild_id, user_id, amount):
   warns = self.GetWarns_(guild_id, user_id)

   if 0 <= amount < len(warns):
      del warns[amount]
      w_coll.update_one(
         {
            'guild_id': guild_id,
            'user_id': user_id
         },
         {
             '$set': {
                'warnings': warns
             }
         }
      )
      return True
   return False