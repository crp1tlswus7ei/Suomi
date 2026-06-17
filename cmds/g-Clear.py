import asyncio
import discord
from typing import Optional
from discord import app_commands
from discord.ext import commands
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
      #
      try:
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
         print(f'Clear: (permissions); {s}')
         return

      # original
      await interaction.response.send_message(
         embed = clearloading_(interaction),
         ephemeral = True
      )

      #
      try:
         clr_ = await interaction.channel.purge(limit = amount)
         msgdel_ = len(clr_)

         await asyncio.sleep(0.5)
         await interaction.edit_original_response(
            embed = clear_(interaction, msgdel_)
         )

      except discord.Forbidden:
         await interaction.followup.send(
            embed = excpcmd_(interaction),
            ephemeral = True,
            view = self.ExcpForbidden
         )
         return
      except Exception as s:
         await interaction.followup.send(
            embed = excperror_(interaction),
            ephemeral = True
         )
         print(f'Clear: (primary); {s}')
         return

#
async def setup(core):
   await core.add_cog(Clear(core))