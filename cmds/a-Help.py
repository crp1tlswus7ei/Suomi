import discord
from discord import app_commands
from discord.ext import commands
from util.Btns import *
from util.Excp import *
from util.Msgs import *

class Help(commands.Cog):
   def __init__(self, core):
      self.core = core

   @app_commands.command(
      name = 'help',
      description = 'Help menu with all Suomi information and command information'
   )
   async def help(self, interaction: discord.Interaction):
      #
      _view = HelpView(interaction)
      #

      await interaction.response.send_message(
         embed = _view.pages[0],
         view = _view
      )

async def setup(core):
   await core.add_cog(Help(core))