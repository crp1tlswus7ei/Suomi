from syst.SysExcp import *
from util.Btns import *
from util.Msgs import *
#
import discord
from discord import app_commands
from discord.ext import commands

class CloneRole(commands.Cog):
   from util.Roles import CloneRole
   def __init__(self, core):
      self.core = core

   @commands.hybrid_command(
      name = 'clone_role',
      aliases = ['clonerole'],
      description = 'Clone a role with all its settings.'
   )
   @app_commands.describe(
      role = 'Role to be cloned.'
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      manage_roles = True
   )
   async def clone_role(
           self,
           ctx: commands.Context,
           role: discord.Role
   ):
      #
      _del = ButtonDeleteCtx(ctx.author)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY)
      _org = ExcpStage(ctx, self, Stage.ORIGINAL)
      _prms = ExcpStage(ctx, self, Stage.PERMISSIONS, overrides = EXCP)
      #
      async with _prms:
         if not ctx.author.guild_permissions.manage_roles:
            raise UserPerms

         if role == ctx.guild.me.top_role:
            raise SuSelfRole

         if role == ctx.guild.default_role:
            raise RoleDefault

         if role >= ctx.author.top_role:
            raise RoleHierarchy

      if _prms.handled:
         return

      #
      async with _org:
         _original = await ctx.send(
            embed = cloneroleloading_(ctx),
            ephemeral = True
         )

      if _org.handled:
         return

      #
      async with _pk:
         await self.CloneRole(ctx, role) # safe

         await _original.edit(
            embed = clonerole_(ctx, role),
            view = _del if not ctx.interaction else None
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(CloneRole(core))