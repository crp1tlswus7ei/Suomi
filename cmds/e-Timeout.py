from syst.SysMute import autoTimeout
from syst.SysExcp import *
from util.Btns import *
from util.Msgs import *
#
import discord
from discord import app_commands
from discord.ext import commands
from datetime import timedelta, datetime, timezone

class Timeout(commands.Cog):
   def __init__(self, core):
      self.core = core

   @commands.hybrid_command(
      name = 'timeout',
      description = 'Mutes a user for certain period of time.'
   )
   @app_commands.describe(
      user = 'User to be muted.',
      duration = 'Minutes of mute; 10 minutes by default.',
      reason = 'Reason for the mute.'
   )
   @app_commands.autocomplete(
      duration = autoTimeout
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      moderate_members = True
   )
   async def timeout(
           self,
           ctx: commands.Context,
           user: discord.Member,
           duration: int = 10,
           reason: str = None
   ):
      #
      ut_ = datetime.now(timezone.utc)
      _del = ButtonDeleteCtx(ctx.author)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY)
      _sec = ExcpStage(ctx, self, Stage.SECONDARY, overrides = EXCP, extra = {'user': user})
      _prms = ExcpStage(ctx, self, Stage.PERMISSIONS, overrides = EXCP)
      #
      async with _prms:
         if not ctx.author.guild_permissions.moderate_members:
            raise UserPerms

         if user == self.core.user:
            raise SuSelf

         if user.id == ctx.author.id:
            raise UserSelf

         if duration <= 0 or duration > 40315:
            raise NullDuration

         if user.top_role >= ctx.author.top_role:
            raise UserHierarchy

      if _prms.handled:
         return

      #
      async with _sec:
         if user.timed_out_until is not None and user.timed_out_until > ut_:
            uttl_ = user.timed_out_until - ut_
            min_ = int(uttl_.total_seconds() // 60)

            _sec.extra['time_left'] = min_
            raise UserTimedOut

      if _sec.handled:
         return

      #
      async with _pk:
         await user.timeout(timedelta(minutes = duration))

         await ctx.send(
            embed = timeout_(ctx, user, duration, reason or 'None'),
            ephemeral = False,
            view = _del
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(Timeout(core))