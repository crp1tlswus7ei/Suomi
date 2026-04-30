import discord
from discord import app_commands
from discord.ext import commands
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class Purge(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.ExcpForbidden = ButtonExcpForbidden()

   @app_commands.command(
      name = 'purge',
      description = 'Delete messages from a specific user without banning them.',
   )
   @app_commands.describe(
      user = 'User to delete messages.'
   )
   @app_commands.default_permissions(
      manage_messages = True,
      moderate_members = True
   )
   async def purge(self, interaction: discord.Interaction, user: discord.Member):
      #
      _delete = ButtonDelete(interaction)

      def check_user(msg):
         return msg.author.id == user.id

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
         print(f'Purge: (permissions); {s}')
         return

      # original
      await interaction.response.send_message(
         embed = purgeloading_(interaction, user),
         ephemeral = True
      )

      #
      try:
         purg_ = await interaction.channel.purge(
            limit = 7049,
            check = check_user
         )
         msgdel_ = len(purg_)

         await interaction.edit_original_response(
            embed = purge_(interaction, user, msgdel_)
         )

      except discord.Forbidden:
         await interaction.followup.send(
            embed = excpcmd_(interaction),
            ephemeral = True,
            view = self.ExcpForbidden
         )
      except Exception as s:
         await interaction.followup.send(
            embed = excperror_(interaction),
            ephemeral = True
         )
         print(f'Purge: (primary); {s}')
         return

#
async def setup(core):
   await core.add_cog(Purge(core))