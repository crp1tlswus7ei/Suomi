from syst.SysExcp import *
from util.Btns import *
from util.Msgs import *
#
import discord
from discord import app_commands
from discord.ext import commands

class Purge(commands.Cog):
   def __init__(self, core):
      self.core = core

   @commands.hybrid_command(
      name = 'purge',
      description = 'Delete messages from a specific user without banning them.',
   )
   @app_commands.describe(
      user = 'User to delete messages.'
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      administrator = True
   )
   async def purge(
           self,
           ctx: commands.Context,
           user: discord.Member
   ):
      #
      _del = ButtonDeleteCtx(ctx.author)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY)
      _org = ExcpStage(ctx, self, Stage.ORIGINAL)
      _prms = ExcpStage(ctx, self, Stage.PERMISSIONS, overrides = EXCP)

      def check_user(msg):
         return msg.author.id == user.id

      #
      async with _prms:
         if not ctx.author.guild_permissions.administrator:
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
      async with _org:
         _original = await ctx.send(
            embed = purgeloading_(ctx, user),
            ephemeral = True,
            view = None
         )

      if _org.handled:
         return

      #
      async with _pk:
         purg_ = await ctx.channel.purge(
            limit = 7049,
            check = check_user
         )
         msgdel_ = len(purg_)

         await _original.edit(
            embed = purge_(ctx, user, msgdel_),
            view = _del if not ctx.interaction else None
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(Purge(core))