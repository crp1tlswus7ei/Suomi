from syst.SysExcp import *
from util.Btns import *
from util.Msgs import *
#
import discord
from discord import app_commands
from discord.ext import commands

class SetMute(commands.Cog):
   from util.Roles import (
      CreateMuteRole,
      CreateHardMuteRole,
      m_over,
      hm_over
   )
   def __init__(self, core):
      self.core = core

   @commands.hybrid_command(
      name = 'set_mute',
      aliases = ['setmute'],
      description = 'Create Mute and Hard Mute roles managed by Suomi.'
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      administrator = True
   )
   async def set_mute(
           self,
           ctx: commands.Context
   ):
      #
      cgr_ = ctx.guild.roles
      cgc_ = ctx.guild.channels
      _view = MenuAdvice(ctx)
      _del = ButtonDeleteCtx(ctx.author)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY)
      _sec = ExcpStage(ctx, self, Stage.SECONDARY)
      _org = ExcpStage(ctx, self, Stage.ORIGINAL)
      _sub = ExcpStage(ctx, self, Stage.SUB)
      _prms = ExcpStage(ctx, self, Stage.PERMISSIONS, overrides = EXCP)

      m_r = discord.utils.get(
         ctx.guild.roles,
         name = 'Mute'
      )
      hm_r = discord.utils.get(
         ctx.guild.roles,
         name = 'Hard Mute'
      )
      #
      async with _prms:
         if not ctx.author.guild_permissions.administrator:
            raise UserPerms

         if m_r in cgr_ or hm_r in cgr_:
            raise RoleExists

      if _prms.handled:
         return

      #
      async with _org:
         _original = await ctx.send(
            embed = setmutecaution_(ctx),
            ephemeral = False,
            view = _view
         )

         await _view.wait()
         if not _view.confirmed:
            await _original.edit(
               embed = excpmenusetmute_(ctx),
               view = _del
            )
            return
         else:
            await _original.edit(
               embed = setmuteloading_(ctx),
               view = None
            )
            pass

      if _org.handled:
         return

      #
      async with _sec:
         await self.CreateMuteRole(ctx) # safe
         m_r = discord.utils.get(
            ctx.guild.roles,
            name = 'Mute'
         )
         for channel in cgc_:
            async with _sub:
               await channel.set_permissions(
                  target = m_r,
                  overwrite = self.m_over
               )
            if _sub.handled:
               pass

         await self.CreateHardMuteRole(ctx) # safe
         hm_r = discord.utils.get(
            ctx.guild.roles,
            name = 'Hard Mute'
         )
         for channel in cgc_:
            async with _sub:
               await channel.set_permissions(
                  target = hm_r,
                  overwrite = self.hm_over
               )
            if _sub.handled:
               pass

      if _sec.handled:
         return

      #
      async with _pk:
         await _original.edit(
            embed = setmute_(ctx),
            view = _del
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(SetMute(core))