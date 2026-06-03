import discord
from typing import Optional
from discord import app_commands
from discord.ext import commands
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
         return
      except Exception as s:
         await interaction.response.send_message(
            embed = excperror_(interaction),
            ephemeral = True
         )
         print(f'ClearWarns: (permissions); {s}')
         return

      #
      if not warns_:
         await interaction.response.send_message(
            embed = excpnullwarns_(interaction, user),
            ephemeral = True
         )
         return

      #
      try:
         await self.Warn.ClearWarns_(
            user.id,
            interaction.guild.id
         )

         await interaction.response.send_message(
            embed = clearwarns_(interaction, user, reason or 'None'),
            ephemeral = False,
            view = _delete
         )

      except discord.Forbidden:
         await interaction.response.send_message(
            embed = excpcmd_(interaction),
            ephemeral = True,
            view = self.ExcpForbidden
         )
         return
      except Exception as s:
         await interaction.response.send_message(
            embed = excperror_(interaction),
            ephemeral = True
         )
         print(f'ClearWarns: (primary); {s}')
         return

#
async def setup(core):
   await core.add_cog(ClearWarns(core))