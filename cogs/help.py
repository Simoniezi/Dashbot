# Made by Simoniezi

# Imports
import os
from dotenv import load_dotenv

import discord
from discord import Member
from discord import embeds
from discord.utils import get
from discord.ext import commands
from discord.errors import Forbidden
from discord.ext.commands import has_permissions, MissingPermissions, MissingRequiredArgument

# Environmental Variables
load_dotenv()

PREFIX = os.getenv('PREFIX')
OWNER = os.getenv('BOT_OWNER_NAME')

async def send_embed(ctx, embed):
    """
    Function that handles the sending of embeds
    -> Takes context and embed to send
    - tries to send embed in channel
    - tries to send normal message when that fails
    - tries to send embed private with information abot missing permissions
    If this all fails: https://youtu.be/dQw4w9WgXcQ
    """
    try:
        await ctx.send(embed=embed)
    except Forbidden:
        try:
            await ctx.send("Hey, seems like I can't send embeds. Please check my permissions :)")
        except Forbidden:
            await ctx.author.send(
                f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
                f"May you inform the server team about this issue? :slight_smile: ", embed=embed)

# Help Handler
class Help(commands.Cog):

    """
    Sends this help message
    """

    # Initialising the file
    def __init__(self, bot):
        self.bot = bot

    # Printing when ready to console
    @commands.Cog.listener()
    async def on_ready(self):
        print('HelpHandler is ready')

    @commands.command(aliases=['commands', 'c'])
    async def _help(self, ctx, *input):
        if not input:
            try:
                owner = ctx.guild.get_member(OWNER).mention

            except AttributeError as e:
                owner = OWNER
        
            emb = discord.Embed(
                title = 'Commands and modules',
                colour = 0x9f00ff,
                description = f'Use `{PREFIX}c <module>` to gain more information about that module ' f':smiley:\n' 
            )

            cogs_desc = ''
            for cog in self.bot.cogs:
                cogs_desc += f'`{cog}` {self.bot.cogs[cog].__doc__}\n'

            emb.add_field(name = 'Modules', value = cogs_desc, inline = True)

            commands_desc = ''
            for command in self.bot.walk_commands():
                if not command.cog_name and not command.hidden:
                    commands_desc += f'{command.name} - {command.help}\n'

          #  if commands_desc:
             #   emb.add_field(name = 'Not belonging to a module', value = commands_desc, inline = False)

        elif len(input) == 1:
            for cog in self.bot.cogs:
                if cog.lower() == input[0].lower():
                    emb = discord.Embed(
                        title = f'{cog} - Commands',
                        description = self.bot.cogs[cog].__doc__,
                        colour = 0x9f00ff
                    )

                    for command in self.bot.get_cog(cog).get_commands():
                        if not command.hidden:
                            emb.add_field(name = f'`{PREFIX}{command.name}`', value = command.help, inline = True)
                    break

            else:
                emb = discord.Embed(
                    title = 'What\'s that!?',
                    description = f'I\'ve never heard from a module called `{input[0]}` before!!',
                    colour = 0x9f00ff
                )

        elif len(input) > 1:
            emb = discord.Embed(
                title = 'That\'s too much.',
                description = 'Please request only one module at once',
                colour = 0x9f00ff
            )

        else:
            emb = discord.Embed(
                title = 'It\'s a magical place.',
                colour = 0x9f00ff
            )

        await send_embed(ctx, emb)

# Adding the cog for main.py to access
def setup(bot):
    bot.add_cog(Help(bot))
