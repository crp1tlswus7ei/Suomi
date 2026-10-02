from syst.SysExcp import *
from util.Btns import *
from util.Msgs import *
#
import discord
from discord import app_commands
from discord.ext import commands

class LockChannel(commands.Cog):
   from util.Roles import overLockdown
   def __init__(self, core):
      self.core = core

   @commands.hybrid_command(
      name = 'lock_channel',
      aliases = [
         'channel_lock',
         'lockchannel',
         'lock',
      ],
      description = 'Locks a channel for sending messages to everyone.'
   )
   @app_commands.describe(
      channel = 'Channel to block messages; Actual by default.',
      reason = 'Reason for lock.'
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      administrator = True
   )
   async def lock_channel(
           self,
           ctx: commands.Context,
           channel: discord.TextChannel = None,
           reason: str = None
   ):
      #
      channel = channel or ctx.channel
      co_ = channel.overwrites_for(ctx.guild.default_role)
      _del = ButtonDeleteCtx(ctx.author)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY, overrides = EXCP)
      _prms = ExcpStage(ctx, self, Stage.PERMISSIONS, overrides = EXCP)
      #
      async with _prms:
         if not ctx.author.guild_permissions.administrator:
            raise UserPerms

      if _prms.handled:
         return

      #
      async with _pk:
         if co_.send_messages is False:
            raise ChannelLocked

         else:
            await channel.set_permissions(
               ctx.guild.default_role,
               overwrite = self.overLockdown
            )

            await ctx.send(
               embed = lockchannel_(ctx, channel, reason or 'None'),
               ephemeral = False,
               view = _del
            )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(LockChannel(core))