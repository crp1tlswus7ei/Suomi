import discord
from discord import app_commands
from discord.ext import commands
from syst.SysExcp import ExcpStage, Stage
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class CloneRole(commands.Cog):
   from util.Roles import CloneRole
   def __init__(self, core):
      self.core = core
      self.ExcpForbiden = ButtonExcpInteraction()

   @app_commands.command(
      name = 'clone_role',
      description = 'Clone a role with all its settings.'
   )
   @app_commands.describe(
      role = 'Role to be cloned.'
   )
   @app_commands.guild_only()
   @app_commands.default_permissions(
      manage_roles = True,
      manage_guild = True,
   )
   async def clone_role(
           self,
           interaction: discord.Interaction,
           role: discord.Role
   ):
      #
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
               embed = excproledefault_(interaction),
               ephemeral = True
            )
            return

         if not interaction.user.guild_permissions.manage_roles:
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
         embed = cloneroleloading_(interaction),
         ephemeral = False
      )

      #
      async with _pk:
         await self.CloneRole(interaction, role) # safe

         await interaction.edit_original_response(
            embed = clonerole_(interaction, role),
            view = _delete
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(CloneRole(core))