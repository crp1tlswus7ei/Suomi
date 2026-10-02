from syst.SysExcp import *
from util.Btns import *
from util.Excp import *
from util.Msgs import *
#
import discord
from discord import app_commands
from discord.ext import commands

class RmMass(commands.Cog):
   def __init__(self, core):
      self.count = 0
      self.core = core

   @commands.hybrid_command(
      name = 'remove_mass',
      aliases = ['removemass'],
      description = 'Remove any role to all users.'
   )
   @app_commands.describe(
      role = 'Role to remove globally.'
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      administrator = True
   )
   async def remove_mass(
           self,
           ctx: commands.Context,
           role: discord.Role
   ):
      #
      cgm_ = ctx.guild.members
      _view = MenuAdvice(ctx)
      _del = ButtonDeleteCtx(ctx.author)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY)
      _sec = ExcpStage(ctx, self, Stage.SECONDARY)
      _org = ExcpStage(ctx, self, Stage.ORIGINAL)
      _prms = ExcpStage(ctx, self, Stage.PERMISSIONS, overrides = EXCP)
      #
      async with _prms:
         if not ctx.author.guild_permissions.administrator:
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
            embed = removemasscaution_(ctx, role),
            ephemeral = False,
            view = _view
         )

      if _org.handled:
         return

      #
      async with _sec:
         await _view.wait()
         if not _view.confirmed:
            await _original.edit(
               embed = excpmenuremovemass_(ctx),
               view = _del
            )
            return
         else:
            await _original.edit(
               embed = removemassloading_(ctx),
               view = None
            )
            pass

      if _sec.handled:
         return

      #
      async with _pk:
         for member in cgm_:
            if role not in member.roles:
               continue

            await member.remove_roles(role)
            self.count += 1

         await _original.edit(
            embed = removemass_(ctx, role),
            view = _del
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(RmMass(core))