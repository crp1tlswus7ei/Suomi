from syst.SysPrefix import *
#
import discord
from discord.ext import commands

class Prefix(commands.Cog):
   def __init__(self, core):
      self.core = core

   @commands.Cog.listener()
   async def on_guild_join(self, guild):
      try:
         await ResetGuildPrefix_(guild.id)

      except Exception as s:
         print(f'On: (GuildPrefix); {s}')
         return

   @commands.Cog.listener()
   async def on_guild_remove(self, guild):
      try:
         await DeletePrefix_(guild.id)

      except Exception as s:
         print(f'Off: (GuildPrefix); {s}')
         return

# Cog
async def setup(core):
   await core.add_cog(Prefix(core))