import discord
from datetime import datetime, timezone
from discord import app_commands
from discord.ext import commands
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class UnTimeout(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.ExcpForbidden = ButtonExcpForbidden()

   @app_commands.command(
      name = 'untimeout',
      description = 'Remove mute from Timeout command.'
   )
   @app_commands.describe(
      user = 'User to be unmuted.',
      reason = 'Reason for unmuting.'
   )
   @app_commands.default_permissions(
      moderate_members = True
   )
   async def untimeout(self, interaction: discord.Interaction, user: discord.Member, reason: str = None):
      #
      ut_ = datetime.now(timezone.utc)
      _delete = ButtonDelete(interaction)
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
         print(f'UnTimeout: (permissions); {s}')
         return

      #
      if user.timed_out_until <= ut_:
         await interaction.response.send_message(
            embed = excpusernotimeout_(interaction, user),
            ephemeral = True
         )
         return

      #
      try:
         await user.timeout(None)

         await interaction.response.send_message(
            embed = untimeout_(interaction, user, reason or 'None'),
            ephemeral = False,
            view = _delete
         )

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
         print(f'UnTimeout: (primary); {s}')
         return

#
async def setup(core):
   await core.add_cog(UnTimeout(core))