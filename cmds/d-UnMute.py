import discord
from typing import Optional
from discord import app_commands
from discord.ext import commands
from syst.SysExcp import ExcpStage, Stage
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class UnMute(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.Mute = core.sMute
      self.ExcpForbidden = ButtonExcpForbidden()

   @app_commands.command(
      name = 'unmute',
      description = 'Unmute a user.',
   )
   @app_commands.describe(
      user = 'User to unmute.',
      reason = 'Reason for unmuting.'
   )
   @app_commands.guild_only()
   @app_commands.default_permissions(
      moderate_members = True,
      manage_roles = True
   )
   async def unmute(
           self,
           interaction: discord.Interaction,
           user: discord.Member,
           reason: Optional[app_commands.Range[str, 1, 70]] = None
   ):
      #
      ur_ = user.roles
      igr_ = interaction.guild.roles
      _delete = ButtonDelete(interaction)
      _pk = ExcpStage(interaction, self, Stage.PRIMARY)
      _prms = ExcpStage(interaction, self, Stage.PERMISSIONS)

      m_r = discord.utils.get(
         interaction.guild.roles,
         name = 'Mute'
      )
      hm_r = discord.utils.get(
         interaction.guild.roles,
         name = 'Hard Mute'
      )
      #
      async with _prms:
         if user == self.core.user:
            await interaction.responses.send_message(
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

      if _prms.handled:
         return

      #
      if m_r not in igr_ or hm_r not in igr_:
         await interaction.response.send_message(
            embed = excprolemutenull_(interaction),
            ephemeral = True
         )
         return

      #
      async with _pk:
         if m_r in ur_:
            await self.Mute.RemoveMute_(user, m_r)

            await interaction.response.send_message(
               embed = unmute_(interaction, user, reason or 'None'),
               ephemeral = False,
               view = _delete
            )
            return

         else:
            if hm_r in ur_:
               await self.Mute.RemoveHardMute_(user, hm_r)

               await interaction.response.send_message(
                  embed = unmute_(interaction, user, reason or 'None'),
                  ephemeral = False,
                  view = _delete
               )
               return

            else:
               await interaction.response.send_message(
                  embed = excpnullmute_(interaction, user),
                  ephemeral = True
               )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(UnMute(core))