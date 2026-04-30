import discord
from datetime import timedelta, datetime, timezone
from discord import app_commands
from discord.ext import commands
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class Timeout(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.ExcpForbidden = ButtonExcpForbidden

   @app_commands.command(
      name = 'timeout',
      description = 'Mutes a user for certain period of time.'
   )
   @app_commands.describe(
      user = 'User to be muted.',
      duration = 'Minutes of mute; 10 minutes by default.',
      reason = 'Reason for the mute.'
   )
   @app_commands.default_permissions(
      moderate_members = True
   )
   async def timeout(self, interaction: discord.Interaction, user: discord.Member, duration: int = 10, reason: str = None):
      #
      ut_ = datetime.now(timezone.utc)
      uttl_ = user.timed_out_until - ut_
      min_ = int(uttl_.total_seconds() // 60)
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

         if duration <= 0 or duration >= 10000:
            await interaction.response.send_message(
               embed = excpnullduration_(interaction),
               ephemeral = True
            )

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
         print(f'Timeout: (permissions); {s}')
         return

      #
      if user.timed_out_until > ut_:
         await interaction.response.send_message(
            embed = excpuseralrtimeout_(interaction, user, min_),
            ephemeral = True
         )
         return

      #
      try:
         await user.timeout(timedelta(minutes = duration))

         await interaction.response.send_message(
            embed = timeout_(interaction, user, duration, reason or 'None'),
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
         print(f'Timeout: (primary); {s}')
         return

#
async def setup(core):
   await core.add_cog(Timeout(core))