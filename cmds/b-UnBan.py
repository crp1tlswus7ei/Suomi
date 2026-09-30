from syst.SysExcp import *
from util.Btns import *
from util.Msgs import *
#
import discord
from discord import app_commands
from discord.ext import commands

class UnBan(commands.Cog):
   def __init__(self, core):
      self.core = core

   @commands.hybrid_command(
      name = 'unban',
      description = 'Lift the ban.'
   )
   @app_commands.describe(
      user_id = 'User ID to be unbanned.'
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      ban_members = True
   )
   async def unban(
           self,
           ctx: commands.Context,
           user_id: str
   ):
      #
      _del = ButtonDeleteCtx(ctx.author)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY)
      _sec = ExcpStage(ctx, self, Stage.SECONDARY, overrides = EXCP)
      _prms = ExcpStage(ctx, self, Stage.PERMISSIONS, overrides = EXCP)
      #
      async with _prms:
         if not ctx.author.guild_permissions.ban_members:
            raise UserPerms

         if user_id == self.core.user.id:
            raise SuSelf

         if user_id == ctx.author.id:
            raise UserSelf

      if _prms.handled:
         return

      #
      async with _sec:
         try:
            toIdUser = int(user_id)
         except ValueError:
            raise IDError

         try:
            user_ = await self.core.fetch_user(toIdUser)
         except discord.HTTPException as s:
            if s.code == 50035:
               raise IDNotFound
            raise

      if _sec.handled:
         return

      #
      async with _pk:
         await ctx.guild.unban(user_)

         await ctx.send(
            embed = unban_(ctx, user_id),
            ephemeral = False,
            view = _del
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(UnBan(core))