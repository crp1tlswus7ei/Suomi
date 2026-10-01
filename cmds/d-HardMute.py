from syst.SysExcp import *
from util.Btns import *
from util.Excp import *
from util.Msgs import *
#
import discord
from discord import app_commands
from discord.ext import commands

class HardMute(commands.Cog):
   def __init__(self, core):
      self.core = core
      self.Mute = core.sMute

   @commands.hybrid_command(
      name = 'hard_mute',
      aliases = [
         'hardmute',
         'hmute'
      ],
      description = 'Mutes a user by removing their roles, indefinitely.'
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
   async def hard_mute(
           self,
           ctx: commands.Context,
           user: discord.Member,
           reason: str = None
   ):
      #
      ur_ = user.roles
      cgr_ = ctx.guild.roles
      _view = MenuAdvice(ctx)
      _del = ButtonDeleteCtx(ctx.author)
      _pk = ExcpStage(ctx, self, Stage.PRIMARY)
      _sec = ExcpStage(ctx, self, Stage.SECONDARY, overrides = EXCP, extra = {'user': user})
      _org = ExcpStage(ctx, self, Stage.ORIGINAL, overrides = EXCP)
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
            raise UserPerms

      if _prms.handled:
         return

      #
      async with _sec:
         if hm_r not in cgr_ or m_r not in cgr_:
            raise NullMuteRoles

         if m_r in ur_:
            raise UserMuted

         if hm_r in ur_:
            raise UserHardMuted

      if _sec.handled:
         return

      #
      async with _org:
         _original = await ctx.send(
            embed = hardmutecaution_(ctx),
            ephemeral = False,
            view = _view
         )

         await _view.wait()
         if not _view.confirmed:
            await _original.edit(
               embed = excpmenuhardmute_(ctx),
               view = _del
            )
            return

         else:
            await _original.edit(
               embed = hardmuteloading_(ctx),
               view = None
            )
            pass

      if _org.handled:
         return

      #
      async with _pk:
         await self.Mute.ApplyHardMute_(user, hm_r)

         await _original.edit(
            embed = hardmute_(ctx, user, reason or 'None'),
            view = _del
         )

      if _pk.handled:
         return

#
async def setup(core):
   await core.add_cog(HardMute(core))