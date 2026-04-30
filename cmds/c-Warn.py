import discord
from discord import app_commands
from discord.ext import commands
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class Warn(commands.Cog):
   from syst.SysWarn import GetWarns_, AddWarns_ # safe
   def __init__(self, core):
      self.core = core
      self.ExcpForbidden = ButtonExcpForbidden()

   @app_commands.command(
      name = 'warn',
      description = 'Add a warn to a user.'
   )
   @app_commands.describe(
      user = 'User to add warn.',
      reason = 'Reason for the warn.'
   )
   @app_commands.default_permissions(
      manage_roles = True
   )
   async def warn(self, interaction: discord.Interaction, user: discord.Member, reason: str):
      #
      user_id = str(user.id)
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

         if not interaction.user.guild_permissions.manage_roles:
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
         print(f'Warn: (permissions); {s}')
         return

      #
      try:
         totalw_ = self.AddWarns_(interaction.guild.id, user_id, reason)  # safe

         await interaction.response.send_message(
            embed = warn_(interaction, user, totalw_, reason),
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
         print(f'Warn: (primary); {s}')
         return

#
async def setup(core):
   await core.add_cog(Warn(core))