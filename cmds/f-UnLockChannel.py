from syst.SysExcp import *
from util.Btns import *
from util.Msgs import *
#
import discord
from discord import app_commands
from discord.ext import commands

class UnLockChannel(commands.Cog):
   from util.Roles import overUnlock
   def __init__(self, core):
      self.core = core

   @commands.hybrid_command(
      name = 'unlock_channel',
      aliases = [
         'channel_unlock',
         'unlockchannel',
         'unlock'
      ],
      description = 'Unlock a locked channel for sending messages.'
   )
   @app_commands.describe(
      channel = 'Channel to unlock; Actual channel by default.',
      reason = 'Reason for unlock.'
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      administrator = True
   )
   async def unlock_channel(
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
         if co_.send_messages:
            raise ChannelUnlocked

         else:
            await channel.set_permissions(
               ctx.guild.default_role,
               overwrite = self.overUnlock
            )

            await ctx.send(
               embed = unlockchannel_(ctx, channel, reason or 'None'),
               ephemeral = False,
               view = _del
            )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(UnLockChannel(core))