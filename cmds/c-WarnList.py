import discord
from discord import app_commands
from discord.ext import commands
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class WarnList(commands.Cog):
   from syst.SysWarn import GetWarns_
   def __init__(self, core):
      self.core = core
      self.ExcpForbidden = ButtonExcpForbidden()

   @app_commands.command(
      name = 'warn_list',
      description = 'Displays a list of all warns for a user.'
   )
   @app_commands.describe(
      user = 'User to display warns.'
   )
   @app_commands.default_permissions(
      manage_roles = True
   )
   async def warn_list(self, interaction: discord.Interaction, user: discord.Member = None):
      #
      user_id = str(user.id)
      user = user or interaction.user
      _delete = ButtonDelete(interaction)
      usrwarns_ = self.GetWarns_(interaction.guild.id, user_id) # safe
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
      except Exception as s:
         await interaction.response.send_message(
            embed = excperror_(interaction),
            ephemeral = True
         )
         print(f'WarnList: (permissions); {s}')
         return

      if not usrwarns_:
         await interaction.response.send_message(
            embed = excpnullwarns_(interaction, user),
            ephemeral = True
         )
         return

      #
      try:
         self.GetWarns_(interaction.guild.id, user_id) # safe

         await interaction.response.send_message(
            embed = warnings_(
               interaction,
               title = f'{user.display_name} warns:',
               description = '\n' + '\n'.join(usrwarns_),
            ),
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
         print(f'WarnList: (primary); {s}')
         return

#
async def setup(core):
   await core.add_cog(WarnList(core))