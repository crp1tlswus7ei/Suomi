from functools import wraps
from util.Btns import *
from util.Excp import *
import asyncio

class Stage:
   PRIMARY = 'primary'
   ORIGINAL = 'original'
   SECONDARY = 'secondary'
   PERMISSIONS = 'permissions'
   SUB = 'sub'

class SuSelf(Exception): pass
class SuSelfRole(Exception): pass
class SuSelfPerms(Exception): pass
#
class ChannelResponse(Exception): pass
class ChannelPerms(Exception): pass
class ChannelLocked(Exception): pass
class ChannelUnlocked(Exception): pass
#
class UserPerms(Exception): pass
class UserNotFound(Exception): pass
class UserNoBan(Exception): pass
class UserSelf(Exception): pass
class UserMuted(Exception): pass
class UserHardMuted(Exception): pass
class UserNoMute(Exception): pass
class UserTimedOut(Exception): pass
class UserNoTimeout(Exception): pass
class UserHierarchy(Exception): pass
#
class RoleHierarchy(Exception): pass
class RoleSetPerms(Exception): pass
class RoleExists(Exception): pass
class RoleDefault(Exception): pass
class RoleDefaultMass(Exception): pass
class RoleDefaultRemoveMass(Exception): pass
#
class IDError(Exception): pass
class IDNotFound(Exception): pass
#
class NullUser(Exception): pass
class NullUserXp(Exception): pass
class NullAmount(Exception): pass
class NullAmountClear(Exception): pass
class NullDuration(Exception): pass
class NullMuteRoles(Exception): pass
class NullWarns(Exception): pass
#
class Menu(Exception): pass
class MenuSetMute(Exception): pass
class MenuMassRole(Exception): pass
class MenuRemoveMass(Exception): pass

#

def _author(target):
   return target.user if isinstance(
      target, discord.Interaction
   ) else target.author

def _delete(target):
   if isinstance(target, discord.Interaction):
      return None
   if isinstance(target, commands.Context) and target.interaction is not None:
      return None
   return ButtonDeleteCtx(_author(target))

def _BuildContext(command, stage):
   return f'{command}: ({stage})' if stage else command

def _Send(target):
   if isinstance(target, discord.Interaction):
      return target.followup.send if target.response.is_done else target.response.send_message
   return target.send

#

async def _Forbidden(target, context, excp, send):
   await send(
      embed = excpcmd_(target),
      ephemeral = True,
      view = ButtonExcpForbidden()
   )
   print(f'{context}; {excp}')

async def _NotFound(target, context, excp, send):
   await send(
      embed = excpusernofound_(target),
      ephemeral = True,
      view = _delete(target)
   )
   print(f'{context}; {excp}')

async def _HTTP(target, context, excp, send):
   await send(
      embed = excperror_(target),
      ephemeral = True,
      view = ButtonExcpHTTP()
   )
   print(f'{context}; {excp}')

async def _ServerError(target, context, excp, send):
   await send(
      embed = excperror_(target),
      ephemeral = True,
      view = _delete(target)
   )
   print(f'{context}: {excp}')

async def _RateLimit(target, context, excp, send):
   await send(
      embed = excperror_(target),
      ephemeral = True,
      view = _delete(target)
   )
   print(f'{context}; {excp}')

async def _Timeout(target, context, excp, send):
   await send(
      embed = excperror_(target),
      ephemeral = True,
      view = _delete(target)
   )
   print(f'{context}; {excp}')

async def _Fallback(target, context, excp, send):
   await send(
      embed = excperror_(target),
      ephemeral = True,
      view = _delete(target)
   )
   print(f'{context}; {excp}')

#

async def _SuSelf(target, context, excp, send):
   await send(
      embed = excpsuomiself_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _SuSelfRole(target, context, excp, send):
   await send(
      embed = excpsuomirole_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _SuSelfPerms(target, context, excp, send):
   await send(
      embed = excpsuomiperms_(target),
      ephemeral = True,
      view = _delete(target)
   )

#

async def _ChannelResponse(target, context, excp, send): # reorder Channel
   await send(
      embed = excpchannelresponse_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _ChannelPerms(target, context, excp, send):
   await send(
      embed = excpchannelperms_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _ChannelLocked(target, context, excp, send):
   await send(
      embed = excpchannelalrlock_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _ChannelUnlocked(target, context, excp, send):
   await send(
      embed = excpchannelnolock_(target),
      ephemeral = True,
      view = _delete(target)
   )

#

async def _UserPerms(target, context, excp, send):
   await send(
      embed = excpuserperms_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _UserNotFound(target, context, excp, send):
   await send(
      embed = excpusernofound_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _UserNoBan(target, context, excp, send):
   await send(
      embed = excpusernoban_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _UserSelf(target, context, excp, send):
   await send(
      embed = excpuserself_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _UserNoMute(target, user, context, excp, send):
   await send(
      embed = excpusernomute_(target, user),
      ephemeral = True,
      view = _delete(target)
   )

async def _UserMuted(target, user, context, excp, send):
   await send(
      embed = excpuseralrmute_(target, user),
      ephemeral = True,
      view = _delete(target)
   )

async def _UserHardMuted(target, user, context, excp, send):
   await send(
      embed = excpuseralrhardmute_(target, user),
      ephemeral = True,
      view = _delete(target)
   )

async def _UserTimedOut(target, user, time_left, context, excp, send):
   await send(
      embed = excpuseralrtimeout_(target, user, time_left),
      ephemeral = True,
      view = _delete(target)
   )

async def _UserNoTimeout(target, user, context, excp, send):
   await send(
      embed = excpusernotimeout_(target, user),
      ephemeral = True,
      view = _delete(target)
   )

async def _UserHierachary(target, context, excp, send):
   await send(
      embed = excpuserhierarchy_(target),
      ephemeral = True,
      view = _delete(target)
   )

#

async def _RoleHierarchy(target, context, excp, send):
   await send(
      embed = excprolehierarchy_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _RoleSetPerms(target, context, excp, send):
   await send(
      embed = excprolesetperms_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _RoleExists(target, context, excp, send):
   await send(
      embed = excprolealrexist_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _RoleDefault(target, context, excp, send):
   await send(
      embed = excproledefault_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _RoleDefaultMass(target, context, excp, send):
   await send(
      embed = excproledefaultinmass_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _RoleDefaultRemoveMass(target, context, excp, send):
   await send(
      embed = excproledefaultinremovemass_(target),
      ephemeral = True,
      view = _delete(target)
   )

#

async def _IDError(target, context, excp, send):
   await send(
      embed = excpiderror_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _IDNotFound(target, context, excp, send):
   await send(
      embed = excpidnofound_(target),
      ephemeral = True,
      view = _delete(target)
   )

#

async def _NullUser(target, context, excp, send):
   await send(
      embed = excpnulluser(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _NullAmount(target, context, excp, send):
   await send(
      embed = excpnullamount_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _NullAmountClear(target, context, excp, send):
   await send(
      embed = excpnullamountinclear_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _NullDuration(target, context, excp, send):
   await send(
      embed = excpnullduration_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _NullMuteRoles(target, user, context, excp, send):
   await send(
      embed = excpnullmuteroles_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _NullWarns(target, user, context, excp, send):
   await send(
      embed = excpnullwarns_(target, user),
      ephemeral = True,
      view = _delete(target)
   )

async def _NullUserXp(target, user, context, excp, send):
   await send(
      embed = excpnulluserxp_(target, user),
      ephemeral = True,
      view = _delete(target)
   )

#

async def _Menu(target, user, context, excp, send):
   await send(
      embed = excpmenu_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _MenuSetMute(target, context, excp, send):
   await send(
      embed = excpmenusetmute_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _MenuMassRole(target, context, excp, send):
   await send(
      embed = excpmenumassrole_(target),
      ephemeral = True,
      view = _delete(target)
   )

async def _MenuRemoveMass(target, context, excp, send):
   await send(
      embed = excpmenuremovemass_(target),
      ephemeral = True,
      view = _delete(target)
   )

#

DEFAULT = {
   discord.Forbidden: _Forbidden,
   discord.NotFound: _NotFound,
   discord.HTTPException: _HTTP,
   discord.DiscordServerError: _ServerError,
   discord.RateLimited: _RateLimit,
   asyncio.TimeoutError: _Timeout
}

EXCP = {
   SuSelf: _SuSelf,
   SuSelfRole: _SuSelfRole,
   SuSelfPerms: _SuSelfPerms,
   #
   ChannelResponse: _ChannelResponse,
   ChannelPerms: _ChannelPerms,
   ChannelLocked: _ChannelLocked,
   ChannelUnlocked: _ChannelUnlocked,
   #
   UserPerms: _UserPerms,
   UserNotFound: _UserNotFound,
   UserNoBan: _UserNoBan,
   UserSelf: _UserSelf,
   UserMuted: _UserMuted,
   UserHardMuted: _UserHardMuted,
   UserNoMute: _UserNoMute,
   UserTimedOut: _UserTimedOut,
   UserNoTimeout: _UserNoTimeout,
   UserHierarchy: _UserHierachary,
   #
   RoleHierarchy: _RoleHierarchy,
   RoleSetPerms: _RoleSetPerms,
   RoleExists: _RoleExists,
   RoleDefault: _RoleDefault,
   RoleDefaultMass: _RoleDefaultMass,
   RoleDefaultRemoveMass: _RoleDefaultRemoveMass,
   #
   IDError: _IDError,
   IDNotFound: _IDNotFound,
   #
   NullUser: _NullUser,
   NullUserXp: _NullUserXp,
   NullAmount: _NullAmount,
   NullAmountClear: _NullAmountClear,
   NullDuration: _NullDuration,
   NullMuteRoles: _NullMuteRoles,
   NullWarns: _NullWarns,
   #
   Menu: _Menu,
   MenuSetMute: _MenuSetMute,
   MenuMassRole: _MenuMassRole,
   MenuRemoveMass: _MenuRemoveMass
}

#

async def _DispatchExcp(
        target,
        context,
        excp,
        overrides = None,
        extra = None
):
   _send = _Send(target)
   _handlers = {**DEFAULT, **(overrides or {})}

   for _exc_type, handler in _handlers.items():
      if isinstance(excp, _exc_type):
         await handler(
            target = target,
            context = context,
            excp = excp,
            send = _send,
            **(extra or {})
         )
         return

   await _Fallback(target, context, excp, _send)

def _HandleExcp(
        stage = None,
        overrides = None
):
   def decorator(func):

      @wraps(func)
      async def wrapper(
              self,
              target: discord.Interaction | commands.Context,
              *args,
              **kwargs
      ):
         try:
            await func(self, target, *args, **kwargs)

         except Exception as s:
            _context = _BuildContext(self.__class__.__name__, stage)
            await _DispatchExcp(target, _context, s, overrides)

      return wrapper
   return decorator

class ExcpStage:
   def __init__(
           self,
           target: discord.Interaction | commands.Context,
           cog,
           stage = None,
           overrides = None,
           extra = None
   ):
      self.target = target
      self.overrides = overrides
      self.extra = extra
      self.context = _BuildContext(cog.__class__.__name__, stage)
      self.handled = False

   async def __aenter__(self):
      return self

   async def __aexit__(self, exc_type, excp, tb):
      if exc_type is None:
         return False

      self.handled = True
      await _DispatchExcp(
         self.target,
         self.context,
         excp,
         self.overrides,
         self.extra
      )
      return True