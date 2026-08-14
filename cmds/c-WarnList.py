import discord
from discord import app_commands
from discord.ext import commands
from syst.SysExcp import ExcpStage, Stage
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
      moderate_members = True,
      manage_roles = True
   )
   async def warn_list(
           self,
           interaction: discord.Interaction,
           user: discord.Member = None
   ):
      #
      user = user or interaction.user
      _pk = ExcpStage(interaction, self, Stage.PRIMARY)
      _sec = ExcpStage(interaction, self, Stage.SECONDARY)
      _prms = ExcpStage(interaction, self, Stage.PERMISSIONS)
      #
      async with _prms:
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

      if _prms.handled:
         return

      #
      async with _sec:
         warns: dict = await self.Warn.GetWarns_(
            user.id,
            interaction.guild_id
         )

      if _sec.handled:
         return

      #
      if not warns:
         await interaction.response.send_message(
            embed = excpnullwarns_(interaction, user),
            ephemeral = True
         )
         return

      #
      async with _pk:
         view = MenuWarns(interaction, user, warns)

         await interaction.response.send_message(
            embed = view._buildEmbed(), # safe
            view = view,
            ephemeral = False
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(WarnList(core))