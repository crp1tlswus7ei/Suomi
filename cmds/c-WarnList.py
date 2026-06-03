import discord
from discord import app_commands
from discord.ext import commands
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class WarnList(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.Warn = core.sWarn
      self.ExcpForbidden = ButtonExcpForbidden()

   @app_commands.command(
      name = 'warn_list',
      description = 'Displays a list of all warns for a user.'
   )
   @app_commands.describe(
      user = 'User to display warns.'
   )
   @app_commands.guild_only()
   @app_commands.default_permissions(
      manage_roles = True
   )
   async def warn_list(
           self,
           interaction: discord.Interaction,
           user: discord.Member = None
   ):
      #
      user = user or interaction.user
      #
      try:
         if user == self.core.user:
            await interaction.response.send_message(
               embed = excpsuomiself_(interaction),
               ephemeral = True
            )
            return

         if not interaction.user.guild_permissions.manage_roles:
            await interaction.response.send_message(
               embed = excpuserperms_(interaction),
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
         print(f'WarnList: (permissions); {s}')
         return

      #
      try:
         warns: dict = await self.Warn.GetWarns_(user.id, interaction.guild_id)
      except Exception as s:
         await interaction.response.send_message(
            embed = excperror_(interaction),
            ephemeral = True
         )
         print(f'WarnList: (secondary); {s}')
         return

      #
      if not warns:
         await interaction.response.send_message(
            embed = excpnullwarns_(interaction, user),
            ephemeral = True
         )
         return

      #
      try:
         view = MenuWarns(interaction, user, warns)

         await interaction.response.send_message(
            embed = view._buildEmbed(), # safe
            view = view,
            ephemeral = False
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
         print(f'WarnList: (primary); {s}')
         return

#
async def setup(core):
   await core.add_cog(WarnList(core))