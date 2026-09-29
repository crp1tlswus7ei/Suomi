"""
You're probably seeing too many warnings about unused parameters; just ignore them.
Interaction exceptions contain an underscore; otherwise, they use context.
"""

import discord
from discord.ext import commands
from util.Ctgr import text

#

def HelpMenuInfo_(ctx: commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = "Hi! I'm Suomi",
      description = 'A customizable, open-source bot designed for server moderation. '
                    'If you want to see my code, visit my GitHub repository. '
                    'Feel free to install it locally, customize it, or add commands, '
                    'and check documentation to learn more about me.',
      color = discord.Color.from_str('#26215C')
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

def HelpMenuCommands_(ctx: commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'About Commands',
      description = f'I currently have 24 commands, all in the moderation category.',
      color = discord.Color.from_str('#26215C')
   )
   embed.add_field(
      name = 'Commands',
      value = f'```{text}```'
   )
   embed.set_footer(
      text = 'Page 2 (Commands)'
   )
   return embed

def HelpMenuSupport_(ctx: commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Support',
      description = "I'll provide comprehensive support for any issues you encounter "
                    "with Suomi or the code, and i'd also appreciate any feedback you "
                    "have about your experience. Thank you for supporting this project.",
      color = discord.Color.from_str('#26215C')
   )
   embed.add_field(
      name = 'Support Links',
      value = '[Email](mailto:oskodev@gmail.com) | '
              '[Support Server](https://discord.gg/KEfpB6yDJN) | '
              '[DM Me](https://discord.com/users/oquattro)'
   )
   embed.set_footer(
      text = '@ Quattro',
      icon_url = ctx.bot.user.display_avatar
   )
   return embed

#

def rank_(
        interaction: discord.Interaction,
        target,
        lv,
        xp,
        xp_need,
        xp_progress,
        xp_range,
        bar,
        percent
      ) -> discord.Embed:
   embed = discord.Embed(
      title = f'{target.display_name} Rank',
      color = discord.Color.from_str('#26215C')
   )
   embed.set_thumbnail(
      url = target.display_avatar.url
   )
   embed.add_field(
      name = 'Level',
      value = f'**{lv}**',
      inline = True
   )
   embed.add_field(
      name = 'XP',
      value = f'**{xp:,}**',
      inline = True
   )
   embed.add_field(
      name = 'Next level:',
      value = f'**{xp_need:,} XP**',
      inline = True
   )
   embed.add_field(
      name = f'Progress ({xp_progress:,} / {xp_range:,})',
      value = f'`{bar}` {percent:.0%}',
      inline = False
   )
   embed.set_footer(
      text = interaction.guild.name,
      icon_url = interaction.guild.icon
   )
   return embed

#

def prefix_(ctx: commands.Context, prefix: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'New Prefix: {prefix}',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'Prefix update by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def prefixactual_(ctx: commands.Context, prefix: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Actual Prefix: {prefix}',
      color = discord.Color.from_str('#06402B')
   )
   return embed

def prefixreset_(ctx: commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = f'Prefix Reset.',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'Reset by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def ban_(ctx: commands.Context, user: discord.Member, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Ban: {user.display_name}',
      description = f'**id:** {user.id}\n'
                    f'**reason:** {reason}',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'Ban by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def kick_(ctx: commands.Context, user: discord.Member, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Kick: {user.display_name}',
      description = f'**id:** {user.id}\n'
                    f'**reason:** {reason}',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'Kick by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def softban_(ctx: commands.Context, user: discord.Member, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'SoftBan: {user.display_name}',
      description = f'**id** {user.id}\n'
                    f'**reason:** {reason}',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'SoftBan by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def unban_(ctx: commands.Context, user_id: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'UnBan: {user_id}',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'UnBan by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def clearwarns_(ctx: commands.Context, user: discord.Member, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'ClearWarns: {user.display_name}',
      description = f'**reason:** {reason}',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'Clean by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def unwarn_(ctx: commands.Context, user: discord.Member, rmc) -> discord.Embed:
   embed = discord.Embed(
      title = f'UnWarn: {user.display_name}',
      description = f'**warns removed:** {rmc}',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'UnWarn by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def warn_(ctx: commands.Context, user: discord.Member, totalw_: int, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Warn: {user.display_name}',
      description = f'**warns:** {totalw_}\n'
                    f'**reason:** {reason}',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'Warn by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def hardmute_(ctx: commands.Context, user: discord.Member, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'HardMute: {user.display_name}',
      description = f'**reason:** {reason}',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'HardMute by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def hardmuteloading_(ctx: commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'HardMute: In progress...',
      color = discord.Color.from_str('#0C447C')
   )
   embed.set_footer(
      text = 'This might take a few seconds.'
   )
   return embed

def hardmutecaution_(ctx: commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'HardMute: Caution',
      color = discord.Color.from_str('#633806')
   )
   embed.set_footer(
      text = "This will remove all user's roles and apply HardMute.\n"
             "(User's roles will be restored once HardMute is removed)."
   )
   return embed

def mute_(ctx: commands.Context, user: discord.Member, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Mute: {user.display_name}',
      description = f'**reason:** {reason}',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'Mute by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def setmute_(ctx: commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'SetMute: Done',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = 'Mute and Hard Mute roles haven been\n'
             'created and permissions been applied.'
   )
   return embed

def setmuteloading_(ctx: commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'SetMute: In progress...',
      color = discord.Color.from_str('#0C447C')
   )
   embed.set_footer(
      text = 'This might take a few seconds.'
   )
   return embed

def setmutecaution_(ctx: commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'SetMute: Caution',
      color = discord.Color.from_str('#633806')
   )
   embed.set_footer(
      text = 'This will create new mute roles\n'
             'configured by Suomi.'
   )
   return embed

def unmute_(ctx: commands.Context, user: discord.Member, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'UnMute: {user.display_name}',
      description = f'**reason:** {reason}',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'UnMute by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def timeout_(ctx: commands.Context, user: discord.Member, duration: int, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Timeout: {user.display_name}',
      description = f'**duration:** {duration} minutes.\n'
                    f'**reason:** {reason}',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'Timeout by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def untimeout_(ctx: commands.Context, user: discord.Member, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'UnTimeout: {user.display_name}',
      description = f'**reason:** {reason}',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'UnTimeout by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def lockchannel_(ctx: commands.Context, channel: discord.TextChannel, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'Lock: {channel.mention}',
      description = f'**reason:** {reason}',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'Lock by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def unlockchannel_(ctx: commands.Context, channel: discord.TextChannel, reason: str) -> discord.Embed:
   embed = discord.Embed(
      title = f'UnLock: {channel.mention}',
      description = f'**reason:** {reason}',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'UnLock by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def clear_(ctx: commands.Context, amount: int) -> discord.Embed:
   embed = discord.Embed(
      title = 'Clear: Done',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'{amount} messages deleted.'
   )
   return embed

def clearloading_(ctx: commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'Clear: In progress...',
      color = discord.Color.from_str('#0C447C')
   )
   embed.set_footer(
      text = 'This might take a few minutes.'
   )
   return embed

def purge_(ctx: commands.Context, user: discord.Member, amount: int) -> discord.Embed:
   embed = discord.Embed(
      title = f'Purge: {user.display_name}',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'{amount} messages deleted.'
   )
   return embed

def purgeloading_(ctx: commands.Context, user: discord.Member) -> discord.Embed:
   embed = discord.Embed(
      title = f'Purge: In progress...',
      color = discord.Color.from_str('#0C447C')
   )
   embed.set_footer(
      text = 'This might take a few minutes.'
   )
   return embed

def clonerole_(ctx: commands.Context, role: discord.Role) -> discord.Embed:
   embed = discord.Embed(
      title = f'CloneRole: Done',
      description = f'**role:** {role.name}',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'Clone by: {ctx.author.display_name}',
      icon_url = ctx.author.avatar
   )
   return embed

def cloneroleloading_(ctx: commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'CloneRole: In progress...',
      color = discord.Color.from_str('#0C447C')
   )
   embed.set_footer(
      text = 'This might take a few seconds.'
   )
   return embed

def massrole_(ctx: commands.Context, role: discord.Role) -> discord.Embed:
   embed = discord.Embed(
      title = 'MassRole: Done',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'"{role}" added globally.'
   )
   return embed

def massroleloading_(ctx: commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'MassRole: In progress...',
      color = discord.Color.from_str('#0C447C')
   )
   embed.set_footer(
      text = 'This might take a few minutes.'
   )
   return embed

def massrolecaution_(ctx: commands.Context, role: discord.Role) -> discord.Embed:
   embed = discord.Embed(
      title = 'MassRole: Caution',
      color = discord.Color.from_str('#633806')
   )
   embed.set_footer(
      text = f'This will add "{role}" to all users, including Bots.'
   )
   return embed

def removemass_(ctx: commands.Context, role: discord.Role) -> discord.Embed:
   embed = discord.Embed(
      title = 'RemoveMass: Done',
      color = discord.Color.from_str('#06402B')
   )
   embed.set_footer(
      text = f'"{role}" removed globally.'
   )
   return embed

def removemassloading_(ctx: commands.Context) -> discord.Embed:
   embed = discord.Embed(
      title = 'RemoveMass: In progress...',
      color = discord.Color.from_str('#0C447C')
   )
   embed.set_footer(
      text = 'This might take a few minutes.'
   )
   return embed

def removemasscaution_(ctx: commands.Context, role: discord.Role) -> discord.Embed:
   embed = discord.Embed(
      title = 'RemoveMass: Caution',
      color = discord.Color.from_str('#633806')
   )
   embed.set_footer(
      text = f'This will remove "{role}" for all users, including Bots.'
   )
   return embed