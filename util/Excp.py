"""
You're probably seeing too many warnings about unused parameters; just ignore them.
Interaction exceptions contain an underscore; otherwise, they use context.
"""

import discord
from discord.ext import commands

#

def excpsuomiself_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = "You can't do that.",
      color = discord.Color.from_str('#791F1F')
   )
   embed.set_footer(
      text = 'You cannot run this command on Suomi.'
   )
   return embed

def excpsuomirole_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = "I can't clone my own role.",
      color = discord.Color.from_str('#791F1F')
   )
   return embed

def excpsuomiperms_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Suomi is not allowed to perform this action.',
      color = discord.Color.from_str('#791F1F')
   )
   embed.set_footer(
      text = 'Check error documentation.'
   )
   return embed

#

def excperror_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Something went wrong.',
      color = discord.Color.from_str('#791F1F')
   )
   embed.set_footer(
      text = 'Try again later or check error documentation.'
   )
   return embed

def excpcmd_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Error executing command.',
      color = discord.Color.from_str('#791F1F')
   )
   embed.set_footer(
      text = 'Try againt later or check error documentation.'
   )
   return embed

def excpchannelresponse_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'You cannot delete this message.',
      color = discord.Color.from_str('#791F1F')
   )
   return embed

def excpchannelperms_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Error modifying channel permissions.',
      color = discord.Color.from_str('#791F1F')
   )
   embed.set_footer(
      text = 'Check Suomi permissions or error documentation.'
   )
   return embed

def excpchannelalrlock_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'This channel is already locked.',
      color = discord.Color.from_str('#6B2E08')
   )
   return embed

def excpchannelnolock_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'This channel is not locked.',
      color = discord.Color.from_str('#6B2E08')
   )
   return embed

#

def excpuserperms_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Insufficient permissions.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Check your permissions or contact a moderator.'
   )
   return embed

def excpusernofound_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Something went wrong.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'User could not be found.'
   )
   return embed

def excpusernoban_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Something went wrong.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'User not banned.'
   )
   return embed

def excpuserself_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = "You can't do that.",
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'You cannot run this command on yourself.'
   )
   return embed

def excpusernomute_(target: discord.Interaction | commands.Context, user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} is not muted.',
      color = discord.Color.from_str('#6B2E08')
   )
   return embed

def excpuseralrmute_(target: discord.Interaction | commands.Context, user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} already muted.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Remove any Mute to apply this.'
   )
   return embed

def excpuseralrhardmute_(target: discord.Interaction | commands.Context, user: discord.Member) -> discord.Member:
   embed = discord.Embed(
      title = f'{user.display_name} already muted.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Remove HardMute to apply Mute.'
   )
   return embed

def excpuseralrtimeout_(target: discord.Interaction | commands.Context, user: discord.Member, time_left) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} already timeout.',
      description = f'**duration:** {time_left} minutes.',
      color = discord.Color.from_str('#6B2E08')
   )
   return embed

def excpusernotimeout_(target: discord.Interaction | commands.Context, user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} has no timeout.',
      color = discord.Color.from_str('#6B2E08')
   )
   return embed

def excpuserhierarchy_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Insufficient permissions by hierarchy.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Check your permissions or contact a moderator.'
   )
   return embed

#

def excprolehierarchy_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Insufficient permissions for this role.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Check your permissions or contact a moderator.'
   )
   return embed

def excprolesetperms_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Something went wrong.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Error configuring role hierarchy.'
   )
   return embed

def excprolealrexist_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Mute or HardMute roles already exists.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Delete old Mute roles to run this command.'
   )
   return embed

def excproledefault_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = "You can't do that",
      color = discord.Color.from_str('#791F1F')
   )
   embed.set_footer(
      text = 'Everyone role cannot be cloned.'
   )
   return embed

def excproledefaultinmass_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = "You can't do that.",
      color = discord.Color.from_str('#791F1F')
   )
   embed.set_footer(
      text = 'Everyone role cannot be added globally.'
   )
   return embed

def excproledefaultinremovemass_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = "You can't do that.",
      color = discord.Color.from_str('#791F1F')
   )
   embed.set_footer(
      text = 'Everyone role cannot be removed.'
   )
   return embed

#

def excpiderror_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Something went wrong.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'The ID cannot contain letters or special characters.'
   )
   return embed

def excpidnofound_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'ID does not exist.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = "This ID does not exist, make sure it's correct."
   )
   return embed

#

def excpnulluser(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'User error.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'The user field cannot be empty.'
   )
   return embed

def excpnulluserxp_(target: discord.Interaction | commands.Context, user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} has no level on this server.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Try again later or send a message to start\n'
             'your level tracking.'
   )
   return embed

def excpnullamount_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Enter a valid amount.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Amount must be less than ten.'
   )
   return embed

def excpnullamountinclear_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Enter a valid amount.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Amount of messages cannot exceed 6k.'
   )
   return embed

def excpnullduration_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Enter a valid duration in minutes.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Duration cannot exceed 4k minutes.'
   )
   return embed

def excpnullmuteroles_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Mute or HardMute roles not found.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Execute "set_mute" command to configure Mute roles.'
   )
   return embed

def excpnullwarns_(target: discord.Interaction | commands.Context, user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} has no warns',
      color = discord.Color.from_str('#6B2E08')
   )
   return embed

#

def excpmenu_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'This menu was no created for you.',
      color = discord.Color.from_str('#6B2E08')
   )
   return embed

def excpmenusetmute_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'SetMute: Operation Canceled.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'No new roles have been created or\n'
             'have any been modified.'
   )
   return embed

def excpmenuhardmute_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'HardMute: Operation Canceled.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'No roles were removed or applied.'
   )
   return embed

def excpmenumassrole_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'MassRole: Operation Canceled.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'No roles were assigned to any users or bots.'
   )
   return embed

def excpmenuremovemass_(target: discord.Interaction | commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'RemoveMass: Operation Canceled.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'No roles were removed from any users or bots.'
   )
   return embed