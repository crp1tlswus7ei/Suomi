from __future__ import annotations
from syst.SysLevel import *
from syst.SysExcp import *
from util.Btns import *
#
import math
import discord
from discord import app_commands
from discord.ext import commands

class Rank(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.Level = core.sLevel

   @commands.hybrid_command(
      name = 'rank',
      description = 'View your current rank on this server.'
   )
   @app_commands.describe(
      user = 'User to review rank.'
   )
   @commands.guild_only()
   async def rank(
           self,
           ctx: commands.Context,
           user: discord.Member = None
   ):
      #
      target = user or ctx.author
      data = await self.Level.GetUserLevel(target.id, ctx.guild.id)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY, extra = {'user': user})
      _delete = ButtonDeleteCtx(ctx.author)

      async with _pk:
         if data is None:
            raise NullUserXp

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
         await ctx.send(
            embed = rank_(
               ctx,
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

      if _pk.handled:
         return

async def setup(core):
   await core.add_cog(Rank(core))