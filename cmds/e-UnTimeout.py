import discord
from typing import Optional
from discord import app_commands
from discord.ext import commands
from syst.SysExcp import ExcpStage, Stage
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
   @app_commands.guild_only()
   @app_commands.default_permissions(
      moderate_members = True
   )
   async def untimeout(
           self,
           interaction: discord.Interaction,
           user: discord.Member,
           reason: Optional[app_commands.Range[str, 1, 70]] = None
   ):
      #
      ut_ = datetime.now(timezone.utc)
      _delete = ButtonDelete(interaction)
      _pk = ExcpStage(interaction, self, Stage.PRIMARY)
      _prms = ExcpStage(interaction, self, Stage.PERMISSIONS)
      #
      async with _prms:
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

      if _prms.handled:
         return

      #
      if user.timed_out_until is None or user.timed_out_until <= ut_:
         await interaction.response.send_message(
            embed = excpusernotimeout_(interaction, user),
            ephemeral = True
         )
         return

      #
      async with _pk:
         await user.timeout(None)

         await interaction.response.send_message(
            embed = untimeout_(interaction, user, reason or 'None'),
            ephemeral = False,
            view = _delete
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(UnTimeout(core))