"""
You're probably seeing too many warnings about unused parameters; just ignore them.
Interaction exceptions contain an underscore; otherwise, they use context.
"""

import discord

def excperror(ctx) -> discord.Embed:
   embed = discord.Embed(
      title = 'Error.',
      color = discord.Color.dark_red()
   )
   embed.set_footer(
      text = 'Check error documentation.'
   )
   return embed

def excpcmd(ctx) -> discord.Embed:
   embed = discord.Embed(
      title = 'Error executing command.',
      color = discord.Color.dark_red()
   )
   embed.set_footer(
      text = 'Check error documentation.'
   )
   return embed

def excpinteraction(ctx) -> discord.Embed:
   embed = discord.Embed(
      title = 'Interaction error.',
      color = discord.Color.dark_red()
   )
   embed.set_footer(
      text = 'Check error documentation.'
   )
   return embed

def excpuserperms(ctx) -> discord.Embed:
   embed = discord.Embed(
      title = 'You are not allowed to use this command.',
      color = discord.Color.dark_red()
   )
   return embed

def excplenprefix(ctx) -> discord.Embed:
   embed = discord.Embed(
      title = 'Prefix cannot have more than 2 characters.',
      color = discord.Color.orange()
   )
   return embed

def excpnoprefix(ctx) -> discord.Embed:
   embed = discord.Embed(
      title = 'New prefix cannot be empty.',
      color = discord.Color.orange()
   )
   return embed

def excpnoamount(ctx) -> discord.Embed:
   embed = discord.Embed(
      title = 'Enter a valid amount',
      color = discord.Color.orange()
   )
   embed.set_footer(
      text = 'The amount must be greater\nthan 0 or less than 10k'
   )
   return embed

#

def excpsuomiself_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = "You cant do that.",
      color = discord.Color.dark_red()
   )
   return embed

def excpsuomirole_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = "I can't clone my own role.",
      color = discord.Color.dark_red()
   )
   return embed

def excpsuomiperms_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Suomi is not allowed to perform this action.',
      color = discord.Color.dark_red()
   )
   embed.set_footer(
      text = 'Check error documentation.'
   )
   return embed

#

def excperror_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Error.',
      color = discord.Color.dark_red()
   )
   embed.set_footer(
      text = 'Check error documentation.'
   )
   return embed

def excpcmd_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Error executing command.',
      color = discord.Color.dark_red()
   )
   embed.set_footer(
      text = 'Check error documentation.'
   )
   return embed

def excpchannel_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Error modifying channel permissions.',
      color = discord.Color.dark_red()
   )
   embed.set_footer(
      text = 'Check error documentation.'
   )
   return embed

def excpchannelalrlock_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'This channel is already locked.',
      color = discord.Color.orange()
   )
   return embed

def excpchannelnolock_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'This channel is not locked.',
      color = discord.Color.orange()
   )
   return embed

def excpinteraction_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Interaction error.',
      color = discord.Color.dark_red()
   )
   embed.set_footer(
      text = 'Check error documentation.'
   )
   return embed

def excpinteractionresp_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'You cannot delete this message.',
      color = discord.Color.dark_red()
   )
   return embed

#

def excpuserperms_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'You are not allowed to use this command.',
      color = discord.Color.orange()
   )
   return embed

def excpusernull_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'You must mention a user.',
      color = discord.Color.orange()
   )
   return embed

def excpusernofound_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'User not found or not banned.',
      color = discord.Color.orange()
   )
   return embed

def excpuserself_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'You cant do that.',
      color = discord.Color.orange()
   )
   return embed

def excpuseralrmute_(interaction: discord.Interaction, user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} already muted.',
      color = discord.Color.orange()
   )
   return embed

def excpuseralrtimeout_(interaction: discord.Interaction, user: discord.Member, time_left) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} already Timed out.',
      description = f'**duration:** {time_left} minutes.',
      color = discord.Color.orange()
   )
   return embed

def excpusernotimeout_(interaction: discord.Interaction, user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} has no Timeout.',
      color = discord.Color.orange()
   )
   return embed

def excpuserinhardmute_(interaction: discord.Interaction, user: discord.Member) -> discord.Member:
   embed = discord.Embed(
      title = f'{user.display_name} already muted.',
      color = discord.Color.orange()
   )
   embed.set_footer(
      text = 'Remove Mute role to apply HardMute.'
   )
   return embed

def excpuserhierarchy_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'You dont have permissions on this user.',
      color = discord.Color.orange()
   )
   return embed

#

def excprolenull_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'You must mention a role.',
      color = discord.Color.orange()
   )
   return embed

def excprolehierarchy_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'You cannot handle this role.',
      color = discord.Color.orange()
   )
   return embed

def excprolesetperms_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Error configuring role hierarchy.',
      color = discord.Color.orange()
   )
   return embed

def excprolemutenull_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Mute or Hard Mute roles not found.',
      color = discord.Color.orange()
   )
   embed.set_footer(
      text = 'Execute "set_mute" extension to\nconfigure Mute roles.'
   )
   return embed

def excprolealrexist_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Mute or Hard Mute roles already exists.',
      color = discord.Color.orange()
   )
   embed.set_footer(
      text = 'Delete old mute roles, and then run this commmand.'
   )
   return embed

def excproledefault_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Everyone role cannot be cloned.',
      color = discord.Color.orange()
   )
   return embed

def excproledefaultinmass_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Everyone role cannot added globally.',
      color = discord.Color.orange()
   )
   return embed

#

def excpiderror_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Invalid ID.',
      color = discord.Color.orange()
   )
   embed.set_footer(
      text = 'ID must no contain letters.'
   )
   return embed

def excpidnull_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'ID cannot be empty.',
      color = discord.Color.orange()
   )
   return embed

def excpidnofound_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'ID does not exist.',
      color = discord.Color.orange()
   )
   embed.set_footer(
      text = 'Make sure the ID is correct.'
   )
   return embed

#

def excpnulltarget_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Target cannot be empty.',
      color = discord.Color.orange()
   )
   return embed

def excpnullamount_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Enter a valid amount.',
      color = discord.Color.orange()
   )
   embed.set_footer(
      text = 'Amount must be greater than zero or\nless than ten.'
   )
   return embed

def excpnullamountinclear_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Enter a valid amount.',
      color = discord.Color.orange()
   )
   embed.set_footer(
      text = 'The amount must be greater\nthan 0 or less than 10k'
   )
   return embed

def excpnullduration_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Enter a valid duration in minutes.',
      color = discord.Color.orange()
   )
   embed.set_footer(
      text = 'Duration must be greater than zero\nor less than 10k minutes.'
   )
   return embed

def excpnullwarns_(interaction: discord.Interaction, user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} has no warns',
      color = discord.Color.orange()
   )
   return embed

def excpnullmute_(interaction: discord.Interaction, user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} is not muted.',
      color = discord.Color.orange()
   )
   return embed

#

def excpmenu_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'This menu was no created for you.',
      color = discord.Color.orange()
   )
   return embed

def excpmenusetmute_(inteaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Set Mute: Operation Canceled.',
      color = discord.Color.orange()
   )
   embed.set_footer(
      text = '''No new roles have been created or\nhave any been modified.'''
   )
   return embed

def excpmenuhardmute_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'HardMute: Operation Canceled.',
      color = discord.Color.orange()
   )
   embed.set_footer(
      text = 'No roles were removed or applied.'
   )
   return embed

def excpmenumassrole_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Mass Role: Operation Canceled.',
      color = discord.Color.orange()
   )
   embed.set_footer(
      text = 'No roles were assigned to any users or bots.'
   )
   return embed

#

def excpauth_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Autorization required: 401',
      color = discord.Color.dark_red()
   )
   return embed

def excpauthverify_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Cant verify authorization.',
      color = discord.Color.dark_red()
   )
   return embed

#

def ExtAlrLoad_(interaction: discord.Interaction, extension: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Already loaded: `{extension}`',
      color = discord.Color.dark_orange()
   )
   return embed

def ExtNotLoad_(interaction: discord.Interaction, extension: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Not loaded: `{extension}`',
      color = discord.Color.dark_orange()
   )
   return embed

def ExtNotFound_(interaction: discord.Interaction, extension: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Not found: `{extension}`',
      color = discord.Color.dark_orange()
   )
   return embed