import discord
from discord import app_commands
from discord.ext import commands
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class Warn(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.Warn = core.sWarn
      self.ExcpForbidden = ButtonExcpForbidden()

   @app_commands.command(
      name = 'warn',
      description = 'Add a warn to a user.'
   )
   @app_commands.describe(
      user = 'User to add warn.',
      reason = 'Reason for the warn.'
   )
   @app_commands.guild_only()
   @app_commands.default_permissions(
      manage_roles = True
   )
   async def warn(
           self,
           interaction: discord.Interaction,
           user: discord.Member,
           reason: app_commands.Range[str, 1, 70]
   ):
      #
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
         return
      except Exception as s:
         await interaction.response.send_message(
            embed = excperror_(interaction),
            ephemeral = True
         )
         print(f'Warn: (permissions); {s}')
         return

      #
      try:
         totalWarns_ = await self.Warn.AddWarns_(
            user.id,
            interaction.guild.id,
            interaction.user.id, reason
         )

         await interaction.response.send_message(
            embed = warn_(interaction, user, totalWarns_, reason),
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
         print(f'Warn: (primary); {s}')
         return

#
async def setup(core):
   await core.add_cog(Warn(core))