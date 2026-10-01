from syst.SysExcp import *
from util.Btns import *
from util.Msgs import *
#
import discord
from discord import app_commands
from discord.ext import commands

class Warn(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.Warn = core.sWarn

   @commands.hybrid_command(
      name = 'warn',
      description = 'Add a warn to a user.'
   )
   @app_commands.describe(
      user = 'User to add warn.',
      reason = 'Reason for the warn.'
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      moderate_members = True,
      manage_roles = True
   )
   async def warn(
           self,
           ctx: commands.Context,
           user: discord.Member,
           reason: str = None
   ):
      #
      _del = ButtonDeleteCtx(ctx.author)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY)
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
      async with _pk:
         totalWarns_ = await self.Warn.AddWarns_(
            user.id,
            ctx.guild.id,
            ctx.author.id,
            reason
         )

         await ctx.send(
            embed = warn_(ctx, user, totalWarns_, reason or 'None'),
            ephemeral = False,
            view = _del
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(Warn(core))