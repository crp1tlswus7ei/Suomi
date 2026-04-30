import discord

overLockdown = discord.PermissionOverwrite(send_messages = False)
overUnlock = discord.PermissionOverwrite(send_messages = True)

#

async def CreateMuteRole(self, interaction: discord.Interaction):
   await interaction.guild.create_role(
      name = 'Mute',
      permissions = discord.Permissions(66560),
      colour = discord.Color.dark_red(),
      hoist = False,
      mentionable = False,
      reason = 'Mute role (keep all roles).'
   )

async def CreateHardMuteRole(self, interaction: discord.Interaction):
   await interaction.guild.create_role(
      name = 'Hard Mute',
      permissions = discord.Permissions(66560),
      colour = discord.Color.dark_red(),
      hoist = False,
      mentionable = False,
      reason = 'Hard mute role (remove all roles).'
   )

async def CloneRole(self, interaction: discord.Interaction, role: discord.Role):
   role_ = await interaction.guild.create_role(
      name = f'{role.name} (clone)',
      permissions = role.permissions,
      colour = role.colour,
      hoist = role.hoist,
      mentionable = role.mentionable,
      reason = f'CloneRole by Suomi; {interaction.user.display_name}'
   )
   await role_.edit(
      position = role.position - 1,
   )

#

m_over = discord.PermissionOverwrite(
   # text
   send_messages = False,
   add_reactions = True,
   create_public_threads = False,
   create_private_threads = False,
   send_messages_in_threads = False,
   embed_links = False,
   attach_files = False,
   # vc
   speak = False,
   connect = True,
   stream = False,
   use_voice_activation = False
)

hm_over = discord.PermissionOverwrite(
   # text
   send_messages = False,
   add_reactions = False,
   create_public_threads = False,
   create_private_threads = False,
   send_messages_in_threads = False,
   embed_links = False,
   attach_files = False,
   # vc
   speak = False,
   connect = False,
   stream = False,
   use_voice_activation = False
)