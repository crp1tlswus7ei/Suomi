import discord
from typing import Optional
from discord import app_commands
from discord.ext import commands
from syst.SysExcp import ExcpStage, Stage
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class Clear(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.ExcpForbidden = ButtonExcpForbidden()

   @app_commands.command(
      name = 'clear',
      description = 'Delete any messages from this channel.'
   )
   @app_commands.describe(
      amount = 'Number of messages to delete; 10 by default.'
   )
   @app_commands.guild_only()
   @app_commands.default_permissions(
      manage_messages = True
   )
   async def clear(
           self,
           interaction: discord.Interaction,
           amount: Optional[app_commands.Range[int, 1, 6000]] = 10
   ):
      #
      _delete = ButtonDelete(interaction)
      _pk = ExcpStage(interaction, self, Stage.PRIMARY)
      _prms = ExcpStage(interaction, self, Stage.PERMISSIONS)
      #
      async with _prms:
         if not interaction.user.guild_permissions.manage_messages:
            await interaction.response.send_message(
               embed = excpuserperms_(interaction),
               ephemeral = True
            )
            return

         if amount <= 0 or amount > 6000:
            await interaction.response.send_message(
               embed = excpnullamountinclear_(interaction),
               ephemeral = True
            )
            return

      if _prms.handled:
         return

      # original
      await interaction.response.send_message(
         embed = clearloading_(interaction),
         ephemeral = True
      )

      #
      async with _pk:
         clr_ = await interaction.channel.purge(limit = amount)
         msgdel_ = len(clr_)

         await interaction.edit_original_response(
            embed = clear_(interaction, msgdel_)
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(Clear(core))