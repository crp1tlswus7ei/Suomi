from syst.SysExcp import *
from util.Btns import *
from util.Msgs import *
#
import discord
from discord import app_commands
from discord.ext import commands

class UnWarn(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.Warn = core.sWarn

   @commands.hybrid_command(
      name = 'unwarn',
      description = 'Removes a warn.'
   )
   @app_commands.describe(
      user = 'User to remove warn.',
      amount = 'Number of warns to remove; 1 by default.',
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      moderate_members = True,
      manage_roles = True
   )
   async def unwarn(
           self,
           ctx: commands.Context,
           user: discord.Member,
           amount: int = 1
   ):
      #
      warns_ = await self.Warn.GetWarns_(user.id, ctx.guild.id)
      amount_ = max(1, min(amount, 10))
      rmc = min(amount_, len(warns_))
      _del = ButtonDeleteCtx(ctx.author)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY)
      _sec = ExcpStage(ctx, self, Stage.SECONDARY, overrides = EXCP, extra = {'user': user})
      _prms = ExcpStage(ctx, self, Stage.PERMISSIONS, overrides = EXCP)
      #
      async with _prms:
         if not ctx.author.guild_permissions.manage_roles:
            raise UserPerms

         if user == self.core.user:
            raise SuSelf

         if user.id == ctx.author.id:
            raise UserSelf

         if amount > 10:
            raise NullAmount

         if user.top_role >= ctx.author.top_role:
            raise UserHierarchy

      if _prms.handled:
         return

      #
      async with _sec:
         if not warns_:
            raise NullWarns

      if _sec.handled:
         return

      #
      async with _pk:
         for _ in range(rmc):
            await self.Warn.RemoveWarn_(
               user.id,
               ctx.guild.id,
               0
            )

         await ctx.send(
            embed = unwarn_(ctx, user, rmc),
            ephemeral = False,
            view = _del
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(UnWarn(core))