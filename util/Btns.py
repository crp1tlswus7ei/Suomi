"""
Ignore the warning about the unused discord import statement;
IDK and IDC what will happen if it weren't there. Also, ignore the warning
that the button parameter isn't used; without this parameter,
the buttons won't work properly, so don't delete them.
"""

import discord

from util.Excp import *

#

class MenuAdvice(discord.ui.View):
   def __init__(
           self,
           interaction: discord.Interaction
   ):
      super().__init__(timeout = None)
      self.confirmed = False
      self.interaction = interaction
      self.author = interaction.user.id

   async def interaction_check(self, interaction: discord.Interaction) -> bool:

      if not interaction.user.id == self.author:
         await interaction.response.send_message(
            embed = excpmenu_(interaction),
            ephemeral = True
         )
         return False
      return True

   @discord.ui.button(
      emoji = '<:white_check:1470874033863262220>',
      style = discord.ButtonStyle.green,
   )
   async def _accept(self, interaction: discord.Interaction, button: discord.ui.Button):
      self.confirmed = True
      await interaction.response.defer()
      self.stop()

   @discord.ui.button(
      emoji = '<:white_cross:1405656979266867210>',
      style = discord.ButtonStyle.red,
   )
   async def _denied(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      self.stop()

#

class ButtonDelete(discord.ui.View):
   def __init__(
           self,
           interaction: discord.Interaction
   ):
      super().__init__(timeout = None)
      self.interaction = interaction
      self.author = interaction.user.id

   async def interaction_check(self, interaction: discord.Interaction) -> bool:

      if interaction.user.id != self.author:
         await interaction.response.send_message(
            embed = excpmenu_(interaction),
            ephemeral = True
         )
         return False
      return True

   @discord.ui.button(
      emoji = '<:white_cross:1405656979266867210>',
      style = discord.ButtonStyle.red,
   )
   async def _delete(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      await interaction.message.delete()
      self.stop()

class ButtonDeleteCtx(discord.ui.View):
   def __init__(
           self,
           author: discord.Member
   ):
      super().__init__(timeout = None)
      self.author = author

   async def interaction_check(self, interaction: discord.Interaction) -> bool:
      if interaction.user.id != self.author.id:
         await interaction.response.send_message(
            embed = excpmenu_(interaction),
            ephemeral = True
         )
         return False
      return True

   @discord.ui.button(
      emoji = '<:white_cross:1405656979266867210>',
      style = discord.ButtonStyle.red,
   )
   async def _delete(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      await interaction.message.delete()

#

class ButtonExcpForbidden(discord.ui.View):
   def __init__(self):
      super().__init__(timeout = None)
      self.add_item(
         discord.ui.Button(
            label = 'Documentation',
            url = 'https://discordpy.readthedocs.io/en/stable/api.html?forbidden#discord.Forbidden'
         )
      )

class ButtonExcpInteraction(discord.ui.View):
   def __init__(self):
      super().__init__(timeout = None)
      self.add_item(
         discord.ui.Button(
            label = 'Documentation',
            url = 'https://discordpy.readthedocs.io/en/stable/api.html#discord.InteractionResponded'
         )
      )