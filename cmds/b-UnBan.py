import discord
from discord import app_commands
from discord.ext import commands
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class UnBan(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.ExcpForbidden = ButtonExcpForbidden()

   @app_commands.command(
      name = 'unban',
      description = 'Lift the ban.'
   )
   @app_commands.describe(
      user_id = 'User ID to be unbanned.'
   )
   @app_commands.default_permissions(
      ban_members = True
   )
   async def unban(self, interaction: discord.Interaction, user_id: str):
      #
      user_ = await self.core.fetch_user(user_id)
      _delete = ButtonDelete(interaction)
      #
      if not interaction.user.guild_permissions.ban_members:
            await interaction.response.send_message(
               embed = excpuserperms_(interaction),
               ephemeral = True
            )
            return

      #
      try:
         user_id = int(user_id) # safe

      except ValueError:
         await interaction.response.send_message(
            embed = excpiderror_(interaction),
            ephemeral = True
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
         print(f'UnBan: (user_id); {s}')
         return

      #
      try:
         await interaction.guild.unban(user_)

         await interaction.response.send_message(
            embed = unban_(interaction, user_id),
            ephemeral = False,
            view = _delete
         )

      except discord.Forbidden:
         await interaction.response.send_message(
            embed = excpcmd_(interaction),
            ephemeral = True,
            view = self.ExcpForbidden
         )
      except discord.NotFound:
         await interaction.response.send_message(
            embed = excpusernofound_(interaction),
            ephemeral = True
         )
      except discord.HTTPException as s:
         if s.code == 50035:
            await interaction.response.send_message(
               embed = excpidnofound_(interaction),
               ephemeral = True
            )
      except Exception as s:
         await interaction.response.send_message(
            embed = excperror_(interaction),
            ephemeral = True
         )
         print(f'UnBan: (primary); {s}')
         return

#
async def setup(core):
   await core.add_cog(UnBan(core))