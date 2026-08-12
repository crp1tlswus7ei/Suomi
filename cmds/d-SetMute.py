import discord
from discord import app_commands
from discord.ext import commands
from syst.SysExcp import ExcpStage, Stage
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class SetMute(commands.Cog):
   from util.Roles import (
      CreateMuteRole,
      CreateHardMuteRole,
      m_over,
      hm_over
   )
   def __init__(self, core):
      self.core = core
      self.ExcpForbidden = ButtonExcpForbidden()

   @app_commands.command(
      name = 'set_mute',
      description = 'Create Mute and Hard Mute roles managed by Suomi.'
   )
   @app_commands.guild_only()
   @app_commands.default_permissions(
      administrator = True
   )
   async def set_mute(
           self,
           interaction: discord.Interaction
   ):
      #
      igr_ = interaction.guild.roles
      igc_ = interaction.guild.channels
      _view = MenuAdvice(interaction)
      _delete = ButtonDelete(interaction)
      _cmr = ExcpStage(interaction, self, Stage.CMR)
      _mr = ExcpStage(interaction, self, Stage.MRSETPERMS)
      _hmr = ExcpStage(interaction, self, Stage.HMRSETPERMS)
      _pk = ExcpStage(interaction, self, Stage.PRIMARY)

      m_r = discord.utils.get(
         interaction.guild.roles,
         name = 'Mute'
      )
      hm_r = discord.utils.get(
         interaction.guild.roles,
         name = 'Hard Mute'
      )
      #
      if not interaction.user.guild_permissions.administrator:
         await interaction.response.send_message(
            embed = excpuserperms_(interaction),
            ephemeral = True
         )
         return

      if m_r in igr_ or hm_r in igr_:
         await interaction.response.send_message(
            embed = excprolealrexist_(interaction),
            ephemeral = True
         )
         return

      # original
      await interaction.response.send_message(
         embed = setmutecaution_(interaction),
         ephemeral = False,
         view = _view
      )

      await _view.wait()
      if not _view.confirmed:
         await interaction.edit_original_response(
            embed = excpmenusetmute_(interaction),
            view = _delete
         )
         return
      else:
         await interaction.edit_original_response(
            embed = setmuteloading_(interaction),
            view = None
         )
         pass

      #
      async with _cmr:
         await self.CreateMuteRole(interaction) # safe
         m_r = discord.utils.get(
            interaction.guild.roles,
            name = 'Mute'
         )
         for channel in igc_:
            async with _mr:
               await channel.set_permissions(
                  target = m_r,
                  overwrite = self.m_over
               )
            if _mr.handled:
               return

         await self.CreateHardMuteRole(interaction) # safe
         hm_r = discord.utils.get(
            interaction.guild.roles,
            name = 'Hard Mute'
         )
         for channel in igc_:
            async with _hmr:
               await channel.set_permissions(
                  target = hm_r,
                  overwrite = self.hm_over
               )
            if _hmr.handled:
               return

      if _cmr.handled:
         return

      #
      async with _pk:
         await interaction.edit_original_response(
            embed = setmute_(interaction),
            view = _delete
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(SetMute(core))