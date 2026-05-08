"""
Ignore the warning about the unused discord import statement;
IDK and IDC what will happen if it weren't there. Also, ignore the warning
that the button parameter isn't used; without this parameter,
the buttons won't work properly, so don't delete them.
"""

import discord

from util.Msgs import *
from util.Excp import *

class HelpView(discord.ui.View):
   def __init__(
           self,
           interaction: discord.Interaction
   ):
      super().__init__(timeout = None)
      self.author = interaction.user.id
      self.interaction = interaction
      self.page = 0
      self.pages = [
         HelpMenuInfo_(interaction),
         HelpMenuCommands_(interaction),
         HelpMenuSupport_(interaction)
      ]
      self.updateBtns()

   async def interaction_check(self, interaction: discord.Interaction) -> bool:
      if interaction.user.id != self.author:
         await interaction.response.send_message(
            embed = excpmenu_(interaction),
            ephemeral = True
         )
         return False
      return True

   def updateBtns(self):
      self._left.disabled = self.page == 0
      self._right.disabled = self.page == len(self.pages) - 1

   async def showPage(self, interaction: discord.Interaction):
      self.updateBtns()
      await interaction.response.edit_message(
         embed = self.pages[self.page],
         view = self
      )

   @discord.ui.button(
      emoji = '<:white_left:1484014305241202738>',
      style = discord.ButtonStyle.gray,
      disabled = True
   )
   async def _left(self, interaction: discord.Interaction, button: discord.ui.Button):
      if self.page > 0:
         self.page -= 1

      await self.showPage(interaction)

   @discord.ui.button(
      emoji = '<:white_cross:1405656979266867210>',
      style = discord.ButtonStyle.red,
   )
   async def _delete(self, interaction: discord.Interaction, button: discord.ui.Button):
      await interaction.response.defer()
      await interaction.message.delete()
      self.stop()

   @discord.ui.button(
      emoji = '<:white_right:1501748298845917205>',
      style = discord.ButtonStyle.gray
   )
   async def _right(self, interaction: discord.Interaction, button: discord.ui.Button):
      if self.page < len(self.pages) - 1:
         self.page += 1

      await self.showPage(interaction)
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