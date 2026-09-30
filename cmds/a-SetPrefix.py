from syst.SysPrefix import *
from syst.SysExcp import *
from util.Btns import *
from util.Msgs import *
#
import discord
from discord import app_commands
from discord.ext import commands

class SetPrefix(commands.Cog):
   def __init__(self, core):
      self.core = core

   @commands.hybrid_command(
      name = 'set_prefix',
      description = 'Change default prefix.',
      aliases = [
         'setprefix',
         'prefix'
      ]
   )
   @app_commands.describe(
      prefix = 'New prefix that refers to Suomi.'
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      administrator = True
   )
   async def set_prefix(
           self,
           ctx: commands.Context,
           prefix: str | None = None
   ):
      #
      gi_ = ctx.guild.id
      _prefix = await GetActualPrefix_(gi_)
      _del = ButtonDeleteCtx(ctx.author)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY)
      _prms = ExcpStage(ctx, self, Stage.PERMISSIONS, overrides = EXCP)
      #
      async with _prms:
         if not ctx.author.guild_permissions.administrator:
            raise UserPerms

         if prefix is None:
            await ctx.send(
               embed = prefixactual_(ctx, _prefix),
               ephemeral = True,
               view = _del if not ctx.interaction else None
            )
            return

      if _prms.handled:
         return

      #
      async with _pk:
         await UpdatePrefix_(ctx, prefix)

         await ctx.send(
            embed = prefix_(ctx, prefix),
            ephemeral = False,
            view = _del
         )

      if _pk.handled:
         return

async def setup(core):
   await core.add_cog(SetPrefix(core))