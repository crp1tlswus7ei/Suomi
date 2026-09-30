from syst.SysExcp import *
from util.Btns import *
from util.Msgs import *
#
import discord
from discord import app_commands
from discord.ext import commands

class ClearWarns(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.Warn = core.sWarn

   @commands.hybrid_command(
      name = 'clear_warns',
      aliases = ['clearwarns'],
      description = 'Clear all warns for a user.'
   )
   @app_commands.describe(
      user = 'User to clear warns.'
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      moderate_members = True,
      manage_roles = True
   )
   async def clear_warns(
           self,
           ctx: commands.Context,
           user: discord.Member,
           reason: str
   ):
      #
      warns_ = await self.Warn.GetWarns_(user.id, ctx.guild.id)
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
         await self.Warn.ClearWarns_(user.id, ctx.guild.id)

         await ctx.send(
            embed = clearwarns_(ctx, user, reason or 'None'),
            ephemeral = False,
            view = _del
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(ClearWarns(core))