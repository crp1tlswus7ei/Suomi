"""
You're probably seeing too many warnings about unused parameters; just ignore them.
Interaction exceptions contain an underscore; otherwise, they use context.
"""

categories = [
   'Ban',
   'Kick',
   'SoftBan',
   'UnBan',
   'Warns',
   'UnWarn',
   'ClearWarns',
   'WarnList',
   'Mute',
   'UnMute',
   'HardMute',
   'SetMute',
   'Timeout',
   'UnTimeout',
   'LockChannel',
   'UnLockChannel',
   'Clear',
   'Purge',
   'CloneRole',
   'MassRole'
]
cols = 2
rows = (len(categories) + cols - 1) // cols
split = [
   categories[i * rows:(i + 1) * rows]
   for i in range(cols)
]
widths = []
for col in split:
   widths.append(
      max(len(item) for item in col) + 4
   )
text = ""
for row in range(rows):
   line = ""
   for col_index, col in enumerate(split):
      try:
         line += col[row].ljust(widths[col_index])
      except IndexError:
         pass

   text += line + "\n"

import discord

def prefixset(ctx, new_prefix: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'New Prefix: {new_prefix}',
      colour = discord.Colour.light_gray()
   )
   embed.set_footer(
      text = f'Prefix update by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def prefixactual(ctx, actual_prefix: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Actual Prefix: {actual_prefix}',
      color = discord.Color.light_gray()
   )
   return embed

def prefixreset(ctx) -> discord.Embed:
   embed = discord.Embed(
      title = 'Prefix reset.',
      description = '**default prefix:** !',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'Prefix reset by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def clear(ctx, amount: int) -> discord.Embed:
   embed = discord.Embed(
      title = 'Clear: Done',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'{amount} messages deleted.'
   )
   return embed

def clearloading(ctx) -> discord.Embed:
   embed = discord.Embed(
      title = 'Deleting messages...',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = 'This might take a few minutes.'
   )
   return embed

#

def HelpMenuInfo_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = "Hi! I'm Suomi",
      description = 'A customizable, open-source bot designed for server moderation.'
                    'If you want to see my code, visit my GitHub repository.'
                    'Feel free to install it locally, customize it, or add commands,'
                    'and check documentation to learn more about me.',
      color = discord.Color.light_gray()
   )
   embed.add_field(
      name = 'My links',
      value = '[GitHub](https://github.com/crp1tlswus7ei/Suomi) | '
              '[Support](https://discord.gg/KEfpB6yDJN)'
   )
   embed.set_footer(
      text = 'Page 1 (Information)'
   )
   return embed

def HelpMenuCommands_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'About Commands',
      description = f'I currently have 21 commands, all in the moderation category.',
      color = discord.Color.light_gray()
   )
   embed.add_field(
      name = 'Commands',
      value = f'```{text}```'
   )
   embed.set_footer(
      text = 'Page 2 (Commands)'
   )
   return embed

def HelpMenuSupport_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Support',
      description = "I'll provide comprehensive support for any issues you encounter"
                    "with Suomi or the code, and i'd also appreciate any feedback you"
                    "have about your experience. Thank you for supporting this project.",
      color = discord.Color.light_gray()
   )
   embed.add_field(
      name = 'Support Links',
      value = '[Email](mailto:oskodev@gmail.com) | '
              '[Support Server](https://discord.gg/KEfpB6yDJN) | '
              '[DM Me](https://discord.com/users/oquattro)'
   )
   embed.set_footer(
      text = '@ Quattro',
      icon_url = interaction.client.user.display_avatar
   )
   return embed

#

def ban_(interaction: disord.Interaction, user: discord.Member, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Ban: {user.display_name}',
      description = f'''**id:** {user.id}\n**reason:** {reason}''',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'Ban by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def kick_(interaction: discord.Interaction, user: discord.Member, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Kick: {user.display_name}',
      description = f'**id:** {user.id}\n**reason:** {reason}',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'Kick by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def softban_(interaction: discord.Interaction, user: discord.Member, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'SoftBan: {user.display_name}',
      description = f'**id** {user.id}\n**reason:** {reason}',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'SoftBan by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def unban_(interaction: discord.Interaction, user_id: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Unban: {user_id}',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'Unban by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def clearwarns_(interaction: discord.Interaction, user: discord.Member, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} warns removed.',
      description = f'**reason:** {reason}',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'Clean by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def unwarn_(interaction: discord.Interaction, user: discord.Member, rmc) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} warn(s) removed.',
      description = f'**warns removed:** {rmc}',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'Unwarn by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def warn_(interaction: discord.Interaction, user: discord.Member, totalw_: int, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'{user.display_name} warned.',
      description = f'**warns:** {totalw_}\n**reason:** {reason}',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'Warn by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def warnings_(interaction: discord.Interaction, title: str, description: str) -> discord.Embed:
   embed = discord.Embed(
      title = title,
      description = description,
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'List request by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def hardmute_(interaction: discord.Interaction, user: discord.Member, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'HardMute: {user.display_name}',
      description = f'**reason:** {reason}',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'HardMute by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def hardmuteloading_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'HardMute: In progress...',
      color = discord.Color.light_gray()
   )
   return embed

def hardmutecaution_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'HardMute: Caution',
      color = discord.Color.orange()
   )
   embed.set_footer(
      text = "This will remove all user's roles and apply HardMute.\n"
             "(User's roles will be restored once HardMute is removed)."
   )
   return embed

def mute_(interaction: discord.Interaction, user: discord.Member, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Mute: {user.display_name}',
      description = f'**reason:** {reason}',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'Mute by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def setmute_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Set Mute: Done',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = 'Mute and Hard Mute roles haven been\ncreated and permissions been applied.'
   )
   return embed

def setmuteloading_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Set Mute: In progress...',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = 'This might take a few seconds.'
   )
   return embed

def setmutecaution_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Set Mute: Caution',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = 'This will create new mute roles\nconfigured by Suomi.'
   )
   return embed

def unmute_(interaction: discord.Interaction, user: discord.Member, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Unmute: {user.display_name}',
      description = f'**reason:** {reason}',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'Unmute by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def timeout_(interaction: discord.Interaction, user: discord.Member, duration: int, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Timeout: {user.display_name}',
      description = f'**duration:** {duration} minutes.\n**reason:** {reason}',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'Timeout by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def untimeout_(interaction: discord.Interaction, user: discord.Member, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'UnTimeout: {user.display_name}',
      description = f'**reason:** {reason}',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'Untimeout by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def lockchannel_(interaction: discord.Interaction, channel: discord.TextChannel, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Lock: {channel.mention}',
      description = f'**reason:** {reason}',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'Lock by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def unlockchannel_(interaction: discord.Interaction, channel: discord.TextChannel, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'UnLock: {channel.mention}',
      description = f'**reason:** {reason}',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'Unlock by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def clear_(interacion: discord.Interaction, amount: int) -> discord.Embed:
   embed = discord.Embed(
      title = 'Clear: Done',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'{amount} messages deleted.'
   )
   return embed

def clearloading_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Clear: In progress...',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = 'This might take a few minutes.'
   )
   return embed

def purge_(interaction: discord.Interaction, user: discord.Member, amount: int) -> discord.Embed:
   embed = discord.Embed(
      title = f'Purge: {user.display_name}',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'{amount} messages deleted.'
   )
   return embed

def purgeloading_(interaction: discord.Interaction, user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'Deleting {user.display_name} messages...',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = 'This might take a few mintutes.'
   )
   return embed

def clonerole_(interaction: discord.Interaction, role: discord.Role) -> discord.Embed:
   embed = discord.Embed(
      title = f'Clone Role: Done',
      description = f'**role:** {role.name}',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'Clone by: {interaction.user.display_name}',
      icon_url = interaction.user.avatar
   )
   return embed

def cloneroleloading_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Clone Role: In progress...',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = 'This might take a few seconds.'
   )
   return embed

def massrole_(interaction: discord.Interaction, role: discord.Role) -> discord.Embed:
   embed = discord.Embed(
      title = 'Mass Role: Done',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'"{role}" added globally.'
   )
   return embed

def massroleloading_(interaction: discord.Interaction) -> discord.Embed:
   embed = discord.Embed(
      title = 'Mass Role: In progress...',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = 'This might take a few minutes.'
   )
   return embed

def massrolecaution_(interaction: discord.Interaction, role: discord.Role) -> discord.Embed:
   embed = discord.Embed(
      title = 'MassRole: Caution',
      color = discord.Color.light_gray()
   )
   embed.set_footer(
      text = f'This will add "{role}" to all users, including Bots.'
   )
   return embed

#

def Load_(interaction: discord.Interaction, extension: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Load: `{extension}`',
      color = discord.Color.light_gray()
   )
   return embed

def ReLoad_(interaction: discord.Interaction, extension: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'ReLoad: `{extension}`',
      color = discord.Color.light_gray()
   )
   return embed

def UnLoad_(interaction: discord.Interaction, extension: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'UnLoad: `{extension}`',
      color = discord.Color.light_gray()
   )
   return embed