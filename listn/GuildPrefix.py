import discord
from discord.ext import commands
from syst.SysPrefix import *

class PrefixJoin(commands.Cog):
   def __init__(self, core):
      self.core = core

   @commands.Cog.listener()
   async def on_guild_join(self, guild):
      try:
         await ResetPrefix_(guild.id)

      except Exception as s:
         print(f'GuildPrefix: (primary); {s}')

# Cog
async def setup(core):
   await core.add_cog(PrefixJoin(core))