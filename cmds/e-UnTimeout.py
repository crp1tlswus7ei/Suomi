from syst.SysExcp import *
from util.Btns import *
from util.Msgs import *
#
import discord
from discord import app_commands
from discord.ext import commands

class UnTimeout(commands.Cog):
   def __init__(self, core):
      self.core = core

   @commands.hybrid_command(
      name = 'untimeout',
      description = 'Remove mute from Timeout command.'
   )
   @app_commands.describe(
      user = 'User to be unmuted.',
      reason = 'Reason for unmuting.'
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      moderate_members = True
   )
   async def untimeout(
           self,
           ctx: commands.Context,
           user: discord.Member,
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

         if user.top_role >= ctx.author.top_role:
            raise UserHierarchy

      if _prms.handled:
         return

      #
      async with _sec:
         if user.timed_out_until is None or user.timed_out_until <= ut_:
            raise UserNoTimeout

      if _sec.handled:
         return

      #
      async with _pk:
         await user.timeout(None)

         await ctx.send(
            embed = untimeout_(ctx, user, reason or 'None'),
            ephemeral = False,
            view = _del
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(UnTimeout(core))