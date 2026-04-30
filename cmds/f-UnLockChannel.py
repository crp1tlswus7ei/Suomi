import discord
from discord import app_commands
from discord.ext import commands
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class UnLockChannel(commands.Cog):
   from util.Roles import overUnlock
   def __init__(self, core):
      self.core = core
      self.ExcpForbidden = ButtonExcpForbidden()

   @app_commands.command(
      name = 'unlock_channel',
      description = 'Unlock a locked channel for sending messages.'
   )
   @app_commands.describe(
      channel = 'Channel to unlock; Actual channel by default.',
      reason = 'Reason for unlock.'
   )
   @app_commands.default_permissions(
      administrator = True
   )
   async def unlock_channel(self, interaction: discord.Interaction, channel: discord.TextChannel = None, reason: str = None):
      #
      channel = channel or interaction.channel
      oc_ = channel.overwrites_for(interaction.guild.default_role)
      _delete = ButtonDelete(interaction)
      #
      if not interaction.user.guild_permissions.administrator:
         await interaction.response.send_message(
            embed = excpuserperms_(interaction),
            ephemeral = True
         )
         return

      #
      try:
         if oc_.send_messages:
            await interaction.response.send_message(
               embed = excpchannelnolock_(interaction),
               ephemeral = True
            )
            return

         else:
            await channel.set_permissions(
               interaction.guild.default_role,
               overwrite = self.overUnlock
            )

            await interaction.response.send_message(
               embed = unlockchannel_(interaction, channel, reason or 'None'),
               ephemeral = False,
               view = _delete
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
         print(f'UnLockChannel: (primary); {s}')
         return

#
async def setup(core):
   await core.add_cog(UnLockChannel(core))