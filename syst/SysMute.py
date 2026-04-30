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
w_coll = db['roles']

async def ApplyHardMute_(self, member, mute_role):
   savedRoles = [
      role.id for role in member.roles
      if role.name != '@everyone' and role.id != mute_role.id
   ]

   w_coll.update_one(
      {
         'guild_id': member.guild.id,
         'user_id': member.id
      },
      {
         '$set': {
            'roles': savedRoles
         }
      },
      upsert = True
   )

   await member.edit(roles = [mute_role])

async def RemoveHardMute_(self, member, mute_role):
   userData = w_coll.find_one(
      {
         'guild_id': member.guild.id,
         'user_id': member.id
      }
   )

   if not userData:
      return False

   roleids_ = userData.get('roles', [])
   restoredRoles = []

   for roleid in roleids_:
      role_ = member.guild.get_role(roleid)
      if role_:
         restoredRoles.append(role_)

   await member.edit(roles = restoredRoles)

   w_coll.delete_one(
      {
         'guild_id': member.guild.id,
         'user_id': member.id
      }
   )

   return True