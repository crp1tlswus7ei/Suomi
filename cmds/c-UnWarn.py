import discord
from discord import app_commands
from discord.ext import commands
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class UnWarn(commands.Cog):
   from syst.SysWarn import GetWarns_, RemoveWarn_
   def __init__(self, core):
      self.core = core
      self.ExcpForbidden = ButtonExcpForbidden()

   @app_commands.command(
      name = 'unwarn',
      description = 'Removes a warn.'
   )
   @app_commands.describe(
      user = 'User to remove warn.',
      amount = 'Number of warns to remove; 1 by default.',
   )
   @app_commands.default_permissions(
      manage_roles = True
   )
   async def unwarn(self, interaction: discord.Interaction, user: discord.Member, amount: int = 1):
      #
      user_id = str(user.id)
      warns_ = self.GetWarns_(interaction.guild.id, user_id) # safe
      amount = max(1, min(amount, 10))
      rmc = min(amount, len(warns_))
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

         if amount <= 0 or amount >= 10:
            await interaction.response.send_message(
               embed = excpnullamount_(interaction),
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
         print(f'UnWarn: (permissions); {s}')
         return

      if not warns_:
         await interaction.response.send_message(
            embed = excpnullwarns_(interaction, user),
            ephemeral = True
         )
         return

      #
      try:
         for _ in range(rmc):
            self.RemoveWarn_(interaction.guild.id, user_id, 0) # safe

         await interaction.response.send_message(
            embed = unwarn_(interaction, user, rmc),
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
         print(f'UnWarn: (primary); {s}')
         return

#
async def setup(core):
   await core.add_cog(UnWarn(core))