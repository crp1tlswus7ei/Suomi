import discord
from discord import app_commands
from discord.ext import commands
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class MassRole(commands.Cog):
   def __init__(self, core):
      self.count = 0
      self.core = core
      self.ExcpForbidden = ButtonExcpForbidden()

   @app_commands.command(
      name = 'mass_role',
      description = 'Assign any role you want to all users.'
   )
   @app_commands.describe(
      role = 'Role to assign globally.'
   )
   @app_commands.default_permissions(
      administrator = True
   )
   async def mass_role(self, interaction: discord.Interaction, role: discord.Role):
      #
      members = interaction.guild.members
      _view = MenuAdvice(interaction)
      _delete = ButtonDelete(interaction)
      #
      try:
         if role == interaction.guild.me.top_role:
            await interaction.response.send_message(
               embed = excpsuomirole_(interaction),
               ephemeral = True
            )
            return

         if role == interaction.guild.default_role:
            await interaction.response.send_message(
               embed = excproledefaultinmass_(interaction),
               ephemeral = True
            )
            return

         if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
               embed = excpuserperms_(interaction),
               ephemeral = True
            )
            return

         if role >= interaction.user.top_role:
            await interaction.response.send_message(
               embed = excprolehierarchy_(interaction),
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
         print(f'MassRole: (permissions); {s}')
         return

      # original
      await interaction.response.send_message(
         embed = massrolecaution_(interaction, role),
         ephemeral = False,
         view = _view
      )

      await _view.wait()
      if not _view.confirmed:
         await interaction.edit_original_response(
            embed = excpmenumassrole_(interaction),
            view = _delete
         )

      else:
         await interaction.edit_original_response(
            embed = massroleloading_(interaction),
            view = None
         )
         pass

      #
      try:
         for member in members:
            await member.add_roles(role)
            self.count += 1

         await interaction.edit_original_response(
            embed = massrole_(interaction, role),
            view = _delete
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
         print(f'MassRole: (permissions); {s}')
         return

#
async def setup(core):
   await core.add_cog(MassRole(core))