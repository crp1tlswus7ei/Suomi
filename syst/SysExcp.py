import discord
from functools import wraps
from util.Btns import *
from util.Msgs import *

class Stage:
   PRIMARY = 'primary'
   SECONDARY = 'secondary'
   CMR = 'CreateMuteRoles'
   PERMISSIONS = 'permissions'
   MRSETPERMS = '[m_r] set_permissions'
   HMRSETPERMS = '[hm_r] set_permissions'
#

async def _forbidden_(interaction, context, exc, send):
   await send(
      embed = excpcmd_(interaction),
      ephemeral = True,
      view = ButtonExcpForbidden()
   )
   print(f'{context}; {exc}')

async def _notfound_(interaction, context, exc, send):
   await send(
      embed = excpnotfound_(interaction),
      ephemeral = True,
      view = None
   )
   print(f'{context}; {exc}')

async def _http_(interaction, context, exc, send):
   await send(
      embed = excperror_(interaction),
      ephemeral = True,
      view = ButtonExcpHTTP()
   )
   print(f'{context}; {exc}')

async def _fallback_(interaction, context, exc, send):
   await send(
      embed = excperror_(interaction),
      ephemeral = True,
      view = None
   )
   print(f'{context}; {exc}')

#

DEFAULT_HANDLERS = {
   discord.Forbidden: _forbidden_,
   discord.NotFound: _notfound_,
   discord.HTTPException: _http_,
}

def _build_context_(command, stage):
   return f'{command}: ({stage})' if stage else command

async def _dispatch_excp(
        interaction,
        context,
        exc,
        overrides = None
):
   _send = interaction.followup.send if interaction.response.is_done() else interaction.response.send_message
   _handlers = {**DEFAULT_HANDLERS, **(overrides or {})}

   for _exc_type, handler in _handlers.items():
      if isinstance(exc, _exc_type):
         await handler(interaction, context, exc, _send)
         return

   await _fallback_(interaction, context, exc, _send)

def _handle_excp(
        stage = None,
        overrides = None
):
   def decorator(func):

      @wraps(func)
      async def wrapper(self, interaction: discord.Interaction, *args, **kwargs):
         try:
            await func(self, interaction, *args, **kwargs)

         except Exception as s:
            _context = _build_context_(self.__class__.__name__, stage)
            await _dispatch_excp(interaction, _context, s, overrides)

      return wrapper
   return decorator

class ExcpStage:
   def __init__(
           self,
           interaction,
           cog,
           stage = None,
           overrides = None
   ):
      self.interaction = interaction
      self.overrides = overrides
      self.context = _build_context_(cog.__class__.__name__, stage)
      self.handled = False

   async def __aenter__(self):
      return self

   async def __aexit__(self, exc_type, exc, tb):
      if exc_type is None:
         return False

      self.handled = True
      await _dispatch_excp(self.interaction, self.context, exc, self.overrides)
      return True