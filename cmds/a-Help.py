from syst.SysExcp import *
from util.Btns import *
#
import discord
from discord.ext import commands

class Help(commands.Cog):
   def __init__(self, core):
      self.core = core

   @commands.guild_only()
   @commands.hybrid_command(
      name = 'help',
      description = 'Help menu with all Suomi information and command information'
   )
   async def help(
           self,
           ctx: commands.Context
   ):
      #
      _view = HelpView(ctx)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY)
      #

      async with _pk:
         await ctx.send(
            embed = _view.pages[0],
            view = _view
         )

      if _pk.handled:
         return

async def setup(core):
   await core.add_cog(Help(core))