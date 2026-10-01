from syst.SysExcp import *
from util.Btns import *
from util.Msgs import *
#
import discord
from typing import Optional
from discord import app_commands
from discord.ext import commands

class Ban(commands.Cog):
   def __init__(self, core):
      self.core = core

   @commands.hybrid_command(
      name = 'ban',
      description = 'Bans a user indefinetely.'
   )
   @app_commands.describe(
      user = 'User to be banned.',
      reason = 'Reason for the ban.'
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      ban_members = True
   )
   async def ban(
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
         if not ctx.author.guild_permissions.ban_members:
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
         await user.ban(reason = reason)

         await ctx.send(
            embed = ban_(ctx, user, reason or 'None'),
            ephemeral = False,
            view = _del
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(Ban(core))