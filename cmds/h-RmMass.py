import discord
from discord import app_commands
from discord.ext import commands
from syst.SysExcp import ExcpStage, Stage
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class RmMass(commands.Cog):
   def __init__(self, core):
      self.count = 0
      self.core = core
      self.ExcpForbidden = ButtonExcpForbidden()

   @app_commands.command(
      name = 'remove_mass',
      description = 'Remove any role to all users.'
   )
   @app_commands.describe(
      role = 'Role to remove globally.'
   )
   @app_commands.default_permissions(
      administrator = True
   )
   async def remove_mass(
           self,
           interaction: discord.Interaction,
           role: discord.Role
   ):
      #
      members = interaction.guild.members
      _view = MenuAdvice(interaction)
      _delete = ButtonDelete(interaction)
      _pk = ExcpStage(interaction, self, Stage.PRIMARY)
      _prms = ExcpStage(interaction, self, Stage.PERMISSIONS)
      #
      async with _prms:
         if role == interaction.guild.me.top_role:
            await interaction.response.send_message(
               embed = excpsuomirole_(interaction),
               ephemeral = True
            )
            return

         if role == interaction.guild.default_role:
            await interaction.response.send_message(
               embed = excproledefaultinremovemass_(interaction),
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

      if _prms.handled:
         return

      # original
      await interaction.response.send_message(
         embed = removemasscaution_(interaction, role),
         ephemeral = False,
         view = _view
      )

      await _view.wait()
      if not _view.confirmed:
         await interaction.edit_original_response(
            embed = excpmenuremovemass_(interaction),
            view = _delete
         )
         return

      else:
         await interaction.edit_original_response(
            embed = removemassloading_(interaction),
            view = None
         )
         pass

      #
      async with _pk:
         for member in members:
            if role not in member.roles:
               continue

            await member.remove_roles(role)
            self.count += 1

         await interaction.edit_original_response(
            embed = removemass_(interaction, role),
            view = _delete
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(RmMass(core))