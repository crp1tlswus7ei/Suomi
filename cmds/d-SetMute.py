import asyncio
import discord
from discord import app_commands
from discord.ext import commands
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
   @app_commands.default_permissions(
      administrator = True
   )
   async def set_mute(self, interaction: discord.Interaction):
      #
      guild = interaction.guild
      igc_ = interaction.guild.channels
      igr_ = interaction.guild.roles
      _view = MenuAdvice(interaction)
      _delete = ButtonDelete(interaction)

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
      if not m_r:
         await self.CreateMuteRole(interaction) # safe
         m_r = discord.utils.get(
            interaction.guild.roles,
            name = 'Mute'
         )
         for channel in igc_:
            try:
               await channel.set_permissions(
                  target = m_r,
                  overwrite = self.m_over
               )
            except discord.Forbidden:
               await interaction.followup.send(
                  embed = excpchannel_(interaction),
                  ephemeral = True
               )
            except Exception as s:
               await interaction.followup.send(
                  embed = excperror_(interaction),
                  ephemeral = True
               )
               print(f'SetMute: [m_r] (set_permissions); {s}')
               return

      if not hm_r:
         await self.CreateHardMuteRole(interaction) # safe
         hm_r = discord.utils.get(
            interaction.guild.roles,
            name = 'Hard Mute'
         )
         for channel in igc_:
            try:
               await channel.set_permissions(
                  target = hm_r,
                  overwrite = self.hm_over
               )
            except discord.Forbidden:
               await interaction.followup.send(
                  embed = excpchannel_(interaction),
                  ephemeral = True
               )
            except Exception as s:
               await interaction.followup.send(
                  embed = excperror_(interaction),
                  ephemeral = True
               )
               print(f'SetMute: [hm_r] (set_permissions); {s}')
               return

      #
      bot_role = guild.me.top_role
      roles = list(reversed(guild.roles))
      bot_idx = roles.index(bot_role)
      newroles = (
         roles[:bot_idx + 1] + [m_r, hm_r] +
         [r for r in roles[bot_idx + 1:] if r != (m_r, hm_r)]
      )
      positions = {}
      for i, role in enumerate(reversed(newroles)):
         positions[role] = i

      #
      try:
         await guild.edit_role_positions(positions)

      except Exception as s:
         await interaction.followup.send(
            embed = excprolesetperms_(interaction),
            ephemeral = True
         )
         print(f'SetMute: (hierarchy); {s}')
         return

      #
      await asyncio.sleep(1)
      await interaction.edit_original_response(
         embed = setmute_(interaction),
         view = _delete
      )
      return

#
async def setup(core):
   await core.add_cog(SetMute(core))