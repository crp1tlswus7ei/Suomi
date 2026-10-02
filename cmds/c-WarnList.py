from syst.SysExcp import *
from util.Btns import *
#
import discord
from discord import app_commands
from discord.ext import commands

class WarnList(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.Warn = core.sWarn

   @commands.hybrid_command(
      name = 'warn_list',
      aliases = ['warnlist'],
      description = 'Displays a list of all warns for a user.'
   )
   @app_commands.describe(
      user = 'User to display warns.'
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      manage_roles = True
   )
   async def warn_list(
           self,
           ctx: commands.Context,
           user: discord.Member = None
   ):
      #
      user = user or ctx.author
      _del = ButtonDeleteCtx(ctx.author)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY)
      _sec = ExcpStage(ctx, self, Stage.SECONDARY, overrides = EXCP, extra = {'user': user})
      _prms = ExcpStage(ctx, self, Stage.PERMISSIONS)
      #
      async with _prms:
         if not ctx.author.guild_permissions.manage_roles:
            raise UserPerms

         if user == self.core.user:
            raise SuSelf

      if _prms.handled:
         return

      #
      async with _sec:
         warns: dict = await self.Warn.GetWarns_(
            user.id,
            ctx.guild.id
         )

         if not warns:
            raise NullWarns

      if _sec.handled:
         return

      #
      async with _pk:
         view = MenuWarns(ctx, user, warns)

         await ctx.send(
            embed = view._buildEmbed(), # safe
            ephemeral = False,
            view = view,
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(WarnList(core))