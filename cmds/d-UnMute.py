from syst.SysExcp import *
from util.Btns import *
from util.Msgs import *
#
import discord
from discord import app_commands
from discord.ext import commands

class UnMute(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.Mute = core.sMute

   @commands.hybrid_command(
      name = 'unmute',
      description = 'Unmute a user.',
   )
   @app_commands.describe(
      user = 'User to unmute.',
      reason = 'Reason for unmuting.'
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      manage_roles = True,
      mute_members = True
   )
   async def unmute(
           self,
           ctx: commands.Context,
           user: discord.Member,
           reason: str = None
   ):
      #
      ur_ = user.roles
      cgr_ = ctx.guild.roles
      _del = ButtonDeleteCtx(ctx.author)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY, overrides = EXCP, extra = {'user': user})
      _sec = ExcpStage(ctx, self, Stage.SECONDARY, overrides = EXCP)
      _prms = ExcpStage(ctx, self, Stage.PERMISSIONS, overrides = EXCP)

      m_r = discord.utils.get(
         ctx.guild.roles,
         name = 'Mute'
      )
      hm_r = discord.utils.get(
         ctx.guild.roles,
         name = 'Hard Mute'
      )
      #
      async with _prms:
         if not ctx.author.guild_permissions.manage_roles:
            raise UserPerms

         if user == self.core.user:
            raise SuSelf

         if user.id == ctx.author.id:
            raise UserSelf

         if user.top_role >= ctx.author.top_role:
            raise UserHierarchy

      if _prms.handled:
         return

      #
      async with _sec:
         if m_r not in cgr_ or hm_r not in cgr_:
            raise NullMuteRoles

      if _sec.handled:
         return

      #
      async with _pk:
         if m_r in ur_:
            await self.Mute.RemoveMute_(user, m_r)

            await ctx.send(
               embed = unmute_(ctx, user, reason or 'None'),
               ephemeral = False,
               view = _del
            )
            return

         else:
            if hm_r in ur_:
               await self.Mute.RemoveHardMute_(user, hm_r)

               await ctx.send(
                  embed = unmute_(ctx, user, reason or 'None'),
                  ephemeral = False,
                  view = _del
               )

            else:
               raise UserNoMute

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(UnMute(core))