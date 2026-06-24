from __future__ import annotations

import math
import discord
from discord import app_commands
from discord.ext import commands
from syst.SysLevel import *
from util.Btns import *
from util.Excp import *

class Rank(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.Level = core.sLevel

   @app_commands.command(
      name = 'rank',
      description = 'View your current rank on this server.'
   )
   @app_commands.describe(
      user = 'User to review rank.'
   )
   @app_commands.guild_only()
   async def rank(
           self,
           interaction: discord.Interaction,
           user: discord.Member = None
   ):
      #
      target = user or interaction.user
      data = await self.Level.GetUserLevel(target.id, interaction.guild.id)
      _delete = ButtonDelete(interaction)

      if data is None:
         await interaction.response.send_message(
            embed = excpnulluserxp_(interaction, user),
            ephemeral = True
         )
         return

      bar_len = 20
      lv = data['lv']
      xp = data['xp']
      xp_need = xpForLevel(lv + 1)
      xp_prev = xpForLevel(lv) if lv > 0 else 0
      xp_progress = xp - xp_prev
      xp_range = xp_need - xp_prev
      percent = min(xp_progress / xp_range, 1.0)
      filled = math.floor(percent * bar_len)
      bar = '█' * filled + '░' * (bar_len - filled)

      #
      await interaction.response.send_message(
         embed = rank_(
            interaction,
            target,
            lv,
            xp,
            xp_need,
            xp_progress,
            xp_range,
            bar,
            percent
         ),
         ephemeral = False,
         view = _delete
      )

async def setup(core):
   await core.add_cog(Rank(core))