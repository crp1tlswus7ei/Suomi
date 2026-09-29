import os
import asyncio
import discord
from discord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
#
from syst.SysMute import Mute
from syst.SysWarn import Warn
from syst.SysLevel import Level
from syst.SysPrefix import GetPrefix_

load_dotenv()
class Su:
   def __init__(self):
      self.folders = (
         'cmds', 'listn'
      )
      self.token = os.getenv('CORE_TOKEN')
      self.mongo_uri = os.getenv('MONGO_URI')
      self.owner_id = os.getenv('OWNER_ID')
      self.shot = AsyncIOMotorClient(self.mongo_uri)
      self.ints = discord.Intents.all()
      self.core = commands.Bot(
         intents = self.ints,
         command_prefix = GetPrefix_,
         help_command = None,
         strip_after_prefix = True,
         owner_id = self.owner_id
      )

      #
      @self.core.event
      async def on_ready():
         print(f'Shot: Online... as; {self.core.user.display_name}')
         await self.core.change_presence(
            activity = discord.CustomActivity(
               name = '/help | su!'
            ),
            status = discord.Status('online')
         )

      @self.core.event
      async def setup_hook():
         try:
            sync_ = await self.core.tree.sync()
            print(f'Shot: Sync_; {len(sync_)} commands.')

         except Exception as s:
            print(f'Shot: (sync_); {s}')

   #
   async def connect_(self):
      try:
         await self.shot.admin.command('ping')
         print(f'Shot: Database Online.')

      except Exception as s:
         print(f'Shot: (connect_); {s}')
         print('Shot: Ignoring database error. (This may cause errors with certain commands.)')

   async def load_(self):
      try:
         for folder in self.folders:
            path = f'./{folder}'

            if not os.path.isdir(path):
               print(f'Suomi: Folder "{folder}" not found. (Continuing anyway.)')
               continue

            for filename in os.listdir(path):
               if not filename.endswith('.py'):
                  continue

               ext_ = f'{folder}.{filename[:-3]}'
               try:
                  await self.core.load_extension(ext_)
               except Exception as s:
                  print(f'Shot: (load_primary); {s}')

      except Exception as s:
         print(f'Shot: (load_); {s}')

   #
   async def shot_(self):
      async with self.core:
         self.core.sMute = Mute(self.mongo_uri)
         self.core.sWarn = Warn(self.mongo_uri)
         self.core.sLevel = Level(self.mongo_uri)
         #
         await self.core.sMute.setup()
         await self.core.sWarn.setup()
         await self.core.sLevel.setup()
         await self.connect_()
         await self.load_()
         await self.core.start(self.token)

asyncio.run(Su().shot_())