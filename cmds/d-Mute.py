from syst.SysExcp import *
from util.Btns import *
from util.Msgs import *
#
import discord
from discord import app_commands
from discord.ext import commands

class Mute(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.Mute = core.sMute

   @commands.hybrid_command(
      name = 'mute',
      description = 'Mute a user indefenitely.'
   )
   @app_commands.describe(
      user = 'User to be muted.',
      reason = 'Reason for the mute.'
   )
   @commands.guild_only()
   @app_commands.default_permissions(
      manage_roles = True,
      mute_members = True
   )
   async def mute(
           self,
           ctx: commands.Context,
           user: discord.Member,
           reason: str = None
   ):
      #
      ur_ = user.roles
      cgr_ = ctx.guild.roles
      _del = ButtonDeleteCtx(ctx.author)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY, overrides = EXCP)
      _sec = ExcpStage(ctx, self, Stage.SECONDARY, overrides = EXCP, extra = {'user': user})
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

         if m_r in ur_:
            raise UserMuted

         if hm_r in ur_:
            raise UserHardMuted

      if _sec.handled:
         return

      #
      async with _pk:
         await self.Mute.ApplyMute(user, m_r)

         await ctx.send(
            embed = mute_(ctx, user, reason or 'None'),
            ephemeral = False,
            view = _del
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(Mute(core))