from syst.SysPrefix import *
from syst.SysExcp import *
from util.Btns import *
from util.Msgs import *
#
import discord
from discord import app_commands
from discord.ext import commands

class ResetPrefix(commands.Cog):
   def __init(self, core):
      self.core = core

   @commands.hybrid_command(
      name = 'reset_prefix',
      description = 'Resets prefix to the default.',
      aliases = [
         'resetprefix',
         'default_prefix',
         'defaultprefix'
      ]
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      administrator = True
   )
   async def reset_prefix(
           self,
           ctx: commands.Context
   ):
      #
      _del = ButtonDeleteCtx(ctx.author)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY)
      _prms = ExcpStage(ctx, self, Stage.PERMISSIONS, overrides = EXCP)
      #
      async with _prms:
         if not ctx.author.guild_permissions.administrator:
            raise UserPerms

      if _prms.handled:
         return

      #
      async with _pk:
         await ResetPrefix_(ctx)

         await ctx.send(
            embed = prefixreset_(ctx),
            ephemeral = False,
            view = _del
         )

      if _pk.handled:
         return

async def setup(core):
   await core.add_cog(ResetPrefix(core))