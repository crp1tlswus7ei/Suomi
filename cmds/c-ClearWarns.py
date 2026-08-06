import discord
from typing import Optional
from discord import app_commands
from discord.ext import commands
from syst.SysExcp import ExcpStage, Stage
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class ClearWarns(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.Warn = core.sWarn
      self.ExcpForbidden = ButtonExcpForbidden()

   @app_commands.command(
      name = 'clear_warns',
      description = 'Clear all warns for a user.'
   )
   @app_commands.describe(
      user = 'User to clear warns.'
   )
   @app_commands.guild_only()
   @app_commands.default_permissions(
      moderate_members = True,
      manage_roles = True
   )
   async def clear_warns(
           self,
           interaction: discord.Interaction,
           user: discord.Member,
           reason: Optional[app_commands.Range[str, 1, 70]] = None
   ):
      #
      warns_ = await self.Warn.GetWarns_(
         user.id,
         interaction.guild.id
      )
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
      if not warns_:
         await interaction.response.send_message(
            embed = excpnullwarns_(interaction, user),
            ephemeral = True
         )
         return

      #
      async with _pk:
         await self.Warn.ClearWarns_(
            user.id,
            interaction.guild.id
         )

         await interaction.response.send_message(
            embed = clearwarns_(interaction, user, reason or 'None'),
            ephemeral = False,
            view = _delete
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(ClearWarns(core))