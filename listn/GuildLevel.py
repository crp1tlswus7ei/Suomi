from __future__ import annotations

import discord
from discord.ext import commands

class LevelsCog(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.levels = core.levels

   @commands.Cog.listener()
   async def on_message(self, message: discord.Message) -> None:
      if message.author.bot:
         return

      result = await self.core.levels.on_message(message)

      if result is not None:
         new_lv, _ = result

         await message.channel.send(
            content = f'{message.author.mention} has reached level {new_lv}!'
         )

async def setup(core):
   await core.add_cog(LevelsCog(core))