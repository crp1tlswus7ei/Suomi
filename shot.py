import os
import asyncio
import discord
from discord.ext import commands
from pymongo import MongoClient
from dotenv import load_dotenv
from syst.SysPrefix import GetPrefix_

load_dotenv()
class Su:
   def __init__(self):
      self.folders = (
         'cmds', 'listn'
      )
      self.token = os.getenv('CORE_TOKEN')
      self.mongo_uri = os.getenv('MONGO_URI')
      self.shot = MongoClient(self.mongo_uri)
      self.ints = discord.Intents.all()
      self.core = commands.Bot(
         intents = self.ints,
         command_prefix = GetPrefix_,
         help_command = None,
         strip_after_prefix = True,
         owner_id = 529441009004707840  # oquattro (Osko)
      )

      # on
      @self.core.event
      async def on_ready():
         print(f'Shot: Online... as; {self.core.user.display_name}')
         await self.core.change_presence(
            activity = discord.CustomActivity(
               name = '/help | sudo!'
            ),
            status = discord.Status('online')
         )
         try:
            sync_ = await self.core.tree.sync()
            print(f'Shot: Sync_; {len(sync_)} commands.')

         except Exception as s:
            print(f'Shot: (sync_); {s}')

   # db
   async def connect_(self):
      try:
         self.shot.admin.command('ping')
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

               # primary
               ext_ = f'{folder}.{filename[:-3]}'
               try:
                  await self.core.load_extension(ext_)
               except Exception as s:
                  print(f'Shot: (load_primary); {s}')

      except Exception as s:
         print(f'Shot: (load_); {s}')

   async def shot_(self):
      async with self.core:
         await self.load_()
         await self.connect_()
         await self.core.start(self.token)

asyncio.run(Su().shot_())