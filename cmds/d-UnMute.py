import discord
from discord import app_commands
from discord.ext import commands
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class UnMute(commands.Cog):
   from syst.SysMute import RemoveHardMute_
   def __init__(self, core):
      self.core = core
      self.ExcpForbidden = ButtonExcpForbidden()

   @app_commands.command(
      name = 'unmute',
      description = 'Unmute a user.',
   )
   @app_commands.describe(
      user = 'User to unmute.',
      reason = 'Reason for unmuting.'
   )
   @app_commands.default_permissions(
      manage_roles = True,
      moderate_members = True
   )
   async def unmute(self, interaction: discord.Interaction, user: discord.Member, reason: str = None):
      #
      ur_ = user.roles
      igr_ = interaction.guild.roles
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
         print(f'UnMute: (permissions); {s}')
         return

      #
      if m_r not in igr_ or hm_r not in igr_:
         await interaction.response.send_message(
            embed = excprolemutenull_(interaction),
            ephemeral = True
         )
         return

      #
      try:
         if m_r in ur_:
            await self.RemoveHardMute_(user, m_r) # safe
            await user.remove_roles(m_r)

            await interaction.response.send_message(
               embed = unmute_(interaction, user, reason or 'None'),
               ephemeral = False,
               view = _delete
            )

         else:
            if hm_r in ur_:
               await self.RemoveHardMute_(user, hm_r) # safe
               await user.remove_roles(hm_r)

               await interaction.response.send_message(
                  embed = unmute_(interaction, user, reason or 'None'),
                  ephemeral = False,
                  view = _delete
               )

            else:
               await interaction.response.send_message(
                  embed = excpuseralrmute_(interaction, user),
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
         print(f'UnMute: (permissions); {s}')
         return

#
async def setup(core):
   await core.add_cog(UnMute(core))