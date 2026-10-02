from syst.SysExcp import *
from util.Btns import *
from util.Msgs import *
#
from discord import app_commands
from discord.ext import commands

class Clear(commands.Cog):
   def __init__(self, core):
      self.core = core

   @commands.hybrid_command(
      name = 'clear',
      description = 'Delete any messages from this channel.'
   )
   @app_commands.describe(
      amount = 'Number of messages to delete; 10 by default.'
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      manage_messages = True
   )
   async def clear(
           self,
           ctx: commands.Context,
           amount: int = 10
   ):
      #
      _original = None
      _del = ButtonDeleteCtx(ctx.author)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY)
      _org = ExcpStage(ctx, self, Stage.ORIGINAL, overrides = EXCP)
      _prms = ExcpStage(ctx, self, Stage.PERMISSIONS, overrides = EXCP)
      #
      async with _prms:
         if not ctx.author.guild_permissions.manage_messages:
            raise UserPerms

         if amount <= 0 or amount > 6000:
            raise NullAmountClear

      if _prms.handled:
         return

      #
      async with _org:
         _original = await ctx.send(
            embed = clearloading_(ctx),
            ephemeral = True
         )

      if _org.handled:
         return

      #
      async with _pk:
         clr_ = await ctx.channel.purge(
            limit = amount,
            check = lambda m:
               _original is None or m.id != _original.id
         )
         msgdel_ = len(clr_)

         await _original.edit(
            embed = clear_(ctx, msgdel_),
            view = _del if not ctx.interaction else None
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(Clear(core))