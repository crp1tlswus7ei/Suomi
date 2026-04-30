import discord
from discord import app_commands
from discord.ext import commands
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class HardMute(commands.Cog):
   from syst.SysMute import ApplyHardMute_
   def __init__(self, core):
      self.core = core
      self.ExcpForbidden = ButtonExcpForbidden()

   @app_commands.command(
      name = 'hard_mute',
      description = 'Mutes a user by removing their roles, indefinitely.'
   )
   @app_commands.describe(
      user = 'User to be muted.',
      reason = 'Reason for the mute.'
   )
   @app_commands.default_permissions(
      manage_roles = True,
      moderate_members = True
   )
   async def hard_mute(self, interaction: discord.Interaction, user: discord.Member, reason: str = None):
      #
      ur_ = user.roles
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
      try:
         if user == self.core.user:
            await interaction.response.send_message(
               embed = excpsuomiself_(interaction),
               ephemeral = True
            )
            return

         if user.id == interaction.user.id:
            await interaction.response.send_message(
               embed = excpuserself_(interaction),
               ephemeral = True
            )
            return

         if not interaction.user.guild_permissions.moderate_members:
            await interaction.response.send_message(
               embed = excpuserperms_(interaction),
               ephemeral = True
            )
            return

         if user.top_role >= interaction.user.top_role:
            await interaction.response.send_message(
               embed = excpuserhierarchy_(interaction),
               ephemeral = True
            )
            return

      except discord.Forbidden:
         await interaction.response.send_message(
            embed = excpcmd_(interaction),
            ephemeral = True,
            view = self.ExcpForbidden
         )
      except Exception as s:
         await interaction.response.send_message(
            embed = excperror_(interaction),
            ephemeral = True
         )
         print(f'HardMute: (permissions); {s}')
         return

      #
      if hm_r not in igr_ or m_r not in igr_:
         await interaction.response.send_message(
            embed = excprolemutenull_(interaction),
            ephemeral = True
         )
         return

      if m_r in ur_:
         await interaction.response.send_message(
            embed = excpuserinhardmute_(interaction, user),
            ephemeral = True
         )
         return

      # original
      await interaction.response.send_message(
         embed = hardmutecaution_(interaction),
         ephemeral = False,
         view = _view
      )

      await _view.wait()
      if not _view.confirmed:
         await interaction.edit_original_response(
            embed = excpmenuhardmute_(interaction),
            view = _delete
         )
         return
      else:
         await interaction.edit_original_response(
            embed = hardmuteloading_(interaction),
            view = None
         )
         pass

      #
      try:
         if hm_r not in ur_:
            await self.ApplyHardMute_(user, hm_r) # safe
            await user.add_roles(hm_r)

            await interaction.edit_original_response(
               embed = hardmute_(interaction, user, reason or 'None'),
               view = _delete
            )

         else:
            await interaction.edit_original_response(
               embed = excpuseralrmute_(interaction, user),
               view = _delete
            )
            return

      except discord.Forbidden:
         await interaction.followup.send(
            embed = excpcmd_(interaction),
            ephemeral = True,
            view = self.ExcpForbidden
         )
      except Exception as s:
         await interaction.followup.send(
            embed = excperror_(interaction),
            ephemeral = True
         )
         print(f'HardMute: (primary); {s}')
         return

#
async def setup(core):
   await core.add_cog(HardMute(core))