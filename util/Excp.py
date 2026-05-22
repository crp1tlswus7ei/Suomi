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
      title = "You can't do that.",
      color = discord.Color.from_str('#791F1F')
   )
   embed.set_footer(
      text = 'You cannot run this command on Suomi.'
   )
   return embed

def excpsuomirole_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = "I can't clone my own role.",
      color = discord.Color.from_str('#791F1F')
   )
   return embed

def excpsuomiperms_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Suomi is not allowed to perform this action.',
      color = discord.Color.from_str('#791F1F')
   )
   embed.set_footer(
      text = 'Check error documentation.'
   )
   return embed

#

def excperror_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Something went wrong.',
      color = discord.Color.from_str('#791F1F')
   )
   embed.set_footer(
      text = 'Try again later or check error documentation.'
   )
   return embed

def excpcmd_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Error executing command.',
      color = discord.Color.from_str('#791F1F')
   )
   embed.set_footer(
      text = 'Try againt later or check error documentation.'
   )
   return embed

def excpchannel_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Error modifying channel permissions.',
      color = discord.Color.from_str('#791F1F')
   )
   embed.set_footer(
      text = 'Check Suomi permissions or error documentation.'
   )
   return embed

def excpchannelalrlock_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'This channel is already locked.',
      color = discord.Color.from_str('#6B2E08')
   )
   return embed

def excpchannelnolock_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'This channel is not locked.',
      color = discord.Color.from_str('#6B2E08')
   )
   return embed

def excpinteractionresp_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'You cannot delete this message.',
      color = discord.Color.from_str('#791F1F')
   )
   return embed

#

def excpuserperms_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Insufficient permissions.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Check your permissions or contact a moderator.'
   )
   return embed

def excpusernofound_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Something went wrong.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'User could not be found.'
   )
   return embed

def excpuserself_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = "You can't do that.",
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'You cannot run this command on yourself.'
   )
   return embed

def excpuseralrmute_(interaction: discord.Interaction, user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} already muted.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Remove HardMute to apply Mute.'
   )
   return embed

def excpuseralrtimeout_(interaction: discord.Interaction, user: discord.Member, time_left) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} already timeout.',
      description = f'**duration:** {time_left} minutes.',
      color = discord.Color.from_str('#6B2E08')
   )
   return embed

def excpusernotimeout_(interaction: discord.Interaction, user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} has no timeout.',
      color = discord.Color.from_str('#6B2E08')
   )
   return embed

def excpuserinhardmute_(interaction: discord.Interaction, user: discord.Member) -> discord.Member:
   embed = discord.Embed(
      title = f'{user.display_name} already muted.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Remove Mutee to apply HardMute.'
   )
   return embed

def excpuserhierarchy_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Insufficient permissions by hierarchy.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Check your permissions or contact a moderator.'
   )
   return embed

#

def excprolehierarchy_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Insufficient permissions for this role.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Check your permissions or contact a moderator.'
   )
   return embed

def excprolesetperms_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Something went wrong.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Error configuring role hierarchy.'
   )
   return embed

def excprolemutenull_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Mute or HardMute roles not found.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Execute "set_mute" command to configure Mute roles.'
   )
   return embed

def excprolealrexist_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Mute or HardMute roles already exists.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Delete old Mute roles to run this command.'
   )
   return embed

def excproledefault_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = "You can't do that",
      color = discord.Color.from_str('#791F1F')
   )
   embed.set_footer(
      text = 'Everyone role cannot be cloned.'
   )
   return embed

def excproledefaultinmass_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = "You can't do that.",
      color = discord.Color.from_str('#791F1F')
   )
   embed.set_footer(
      text = 'Everyone role cannot be added globally.'
   )
   return embed

#

def excpiderror_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Something went wrong.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'The ID cannot contain letters or special characters.'
   )
   return embed

def excpidnofound_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'ID does not exist.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = "This ID does not exist, make sure it's correct."
   )
   return embed

#

def excpnullamount_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Enter a valid amount.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Amount must be greater than zero or\nless than ten.'
   )
   return embed

def excpnullamountinclear_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Enter a valid amount.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Amount of messages cannot exceed 10k.'
   )
   return embed

def excpnullduration_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Enter a valid duration in minutes.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Duration cannot exceed 10k minutes.'
   )
   return embed

def excpnullwarns_(interaction: discord.Interaction, user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} has no warns',
      color = discord.Color.from_str('#6B2E08')
   )
   return embed

def excpnullmute_(interaction: discord.Interaction, user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} is not muted.',
      color = discord.Color.from_str('#6B2E08')
   )
   return embed

def excpnulluserxp_(interaction: discord.Interaction, user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} has no level on this server.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'Try again later or send a message to start\n'
             'your level tracking.'
   )
   return embed

#

def excpmenu_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'This menu was no created for you.',
      color = discord.Color.from_str('#6B2E08')
   )
   return embed

def excpmenusetmute_(inteaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'SetMute: Operation Canceled.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'No new roles have been created or\n'
             'have any been modified.'
   )
   return embed

def excpmenuhardmute_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'HardMute: Operation Canceled.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'No roles were removed or applied.'
   )
   return embed

def excpmenumassrole_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'MassRole: Operation Canceled.',
      color = discord.Color.from_str('#6B2E08')
   )
   embed.set_footer(
      text = 'No roles were assigned to any users or bots.'
   )
   return embed

#

def excpauth_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Autorization required.',
      color = discord.Color.from_str('#791F1F')
   )
   return embed

def excpauthverify_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Cant verify authorization.',
      color = discord.Color.from_str('#791F1F')
   )
   return embed

#

def ExtAlrLoad_(interaction: discord.Interaction, extension: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Already loaded: `{extension}`',
      color = discord.Color.from_str('#791F1F')
   )
   return embed

def ExtNotLoad_(interaction: discord.Interaction, extension: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Not loaded: `{extension}`',
      color = discord.Color.from_str('#791F1F')
   )
   return embed

def ExtNotFound_(interaction: discord.Interaction, extension: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Not found: `{extension}`',
      color = discord.Color.from_str('#791F1F')
   )
   return embed