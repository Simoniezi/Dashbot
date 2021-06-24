# Made by Simoniezi

# Imports
import os
from dotenv import load_dotenv

import random

import asyncio

import discord
from discord import Member
from discord import embeds
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, MissingRequiredArgument
# Loading Environmental Variables
load_dotenv()

BOT_OWNER_NAME = os.getenv('BOT_OWNER_NAME')

# Moderation Handler
class Moderation(commands.Cog):

    """
    Classic moderation commands
    """

    # Initialising the file
    def __init__(self, bot):
        self.bot = bot

    # Printing when ready to console
    @commands.Cog.listener()
    async def on_ready(self):
        print('ModerationHandler is ready\n')

    # Clear chat command
    @commands.command(aliases=['purge'])
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):

        """Typical purge/clear command to clear large portions of the chat at once. Max 100 messages at once."""

        # Command action
        await ctx.channel.purge(limit=int(amount) + 1)

        # Priting to console
        print('Clear command used')

    # Clear chat error handler
    @clear.error
    async def clear_error(self, ctx, error):

        # Checks if user is missing permissions
        if isinstance(error, MissingPermissions):

            # Design
            embedVar = discord.Embed(
                title='Insufficient Permission',
                description=f'{ctx.message.author.mention}, you do not have permission to perform this command',
                colour=0xe74c3c
            )
            embedVar.add_field(name='Issue', value='If you believe this is a mistake\nPlease contact a staff member')

            # Message sending
            await ctx.send(embed=embedVar)

            # Printing to console
            print(f'{ctx.message.author} is missing permissions')

    # Kick command
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        
        """A typical kick command. Working as you would expect it to."""

        # Design
        embedVar = discord.Embed(
            title='Member has been kicked',
            description=f'by {ctx.message.author.mention}',
            colour=0x9f00ff
        )
        embedVar.add_field(name='Member kicked:', value=f'{member.mention}')
        embedVar.add_field(name='Reason:', value=f'{reason}')

        # Command action
        await member.kick(reason=reason)

        # Message sending
        await ctx.send(embed=embedVar)

        # Printing to console
        print('Kick command used')

    # Kick error handler
    @kick.error
    async def kick_error(self, ctx, error):

        # Checks if user is missing permissions
        if isinstance(error, MissingPermissions):

            # Design
            embedVarP = discord.Embed(
                title='Insufficient Permission',
                description=f'{ctx.message.author.mention}, you do not have permission to perform this command',
                colour=0xe74c3c
            )
            embedVarP.add_field(name='Issue', value='If you believe this is a mistake\nPlease contact a staff member')

            # Message sending
            await ctx.send(embed=embedVarP)

            # Printing to console
            print(f'{ctx.message.author} is missing permission')

        # Checks if command usage is missing required arguments
        if isinstance(error, commands.MissingRequiredArgument):

            # Design
            embedVarA = discord.Embed(
                title='Missing Argument',
                colour=0xe74c3c
            )
            embedVarA.add_field(name='Issue:', value=f'{ctx.message.author.mention}, you need to mention a member to kick them!')

            # Message sending
            await ctx.send(embed=embedVarA)

            # Printing to console
            print(f'{ctx.message.author} is missing required arguments')

    # Ban command
    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):

        """Excatly what the name suggests. Use this to ban a member, but use it with care."""

        # DM message design
        banned = f'You have been banned from {ctx.guild.name} for {reason}'

        # Design
        embedVar = discord.Embed(
            title='Member has been banned',
            description=f'by {ctx.message.author.mention}',
            colour=0x9f00ff
        )
        embedVar.add_field(name='Member banned:', value=f'{member.mention}')
        embedVar.add_field(name='Reason:', value=f'{reason}')

        # Command action
        await member.ban(reason=reason)

        # DM message sending
        await member.send(banned)

        # Message sending
        await ctx.send(embed=embedVar)

        # Printing to console
        print('Ban command used')
        print(f'{member} was banned')

    # Ban error handler
    @ban.error
    async def ban_error(self, ctx, error):

        # Checks if user is missing permission
        if isinstance(error, MissingPermissions):

            # Design
            embedVarP = discord.Embed(
                title='Insufficient Permission',
                description=f'{ctx.message.author.mention}, you do not have permission to perform this command',
                colour=0xe74c3c
            )
            embedVarP.add_field(name='Issue', value='If you believe this is a mistake\nPlease contact a staff member')

            # Message sending
            await ctx.send(embed=embedVarP)

            # Printing to console
            print(f'{ctx.message.author} is missing permission')

        # Checks if command usage is missing required arguments
        if isinstance(error, commands.MissingRequiredArgument):

            # Design
            embedVarA = discord.Embed(
                title='Missing Argument',
                colour=0xe74c3c
            )
            embedVarA.add_field(name='Issue:', value=f'{ctx.message.author.mention}, you need to mention a member to ban them!')

            # Message sending
            await ctx.send(embed=embedVarA)

            # Printing to console
            print(f'{ctx.message.author} is missing required arguments')

    # Unban command
    @commands.command()
    @has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):

        """Unban a member using their name and discriminator!"""

        # Variables
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):

                # Design
                embedVar = discord.Embed(
                    title='Unban',
                    description=f'by {ctx.message.author.mention}',
                    colour=0x9f00ff
                )
                embedVar.add_field(name='User unbanned:', value=f'{user.mention}')

                # Command action
                await ctx.guild.unban(user)

                # Message sending
                await ctx.send(embed=embedVar)

                #Printing to console
                print('Unban command used')
                print(f'{ctx.member} was unbanned')
                
                return # Weird return here that I don't know what is doing

    # Unban error handler
    @unban.error
    async def unban_error(self, ctx, error):

        # Checks if user is missing permission
        if isinstance(error, MissingPermissions):

            # Design
            embedVarP = discord.Embed(
                title='Insufficient Permission',
                description=f'{ctx.message.author.mention}, you do not have permission to perform this command',
                colour=0xe74c3c
            )
            embedVarP.add_field(name='Issue', value='If you believe this is a mistake\nPlease contact a staff member')

            # Message sending
            await ctx.send(embed=embedVarP)

            # Printing to console
            print(f'{ctx.message.author} is missing permission')

        # Checks if command usage is missing required arguments
        if isinstance(error, commands.MissingRequiredArgument):

            # Design
            embedVarA = discord.Embed(
                title='Missing Argument',
                colour=0xe74c3c
            )
            embedVarA.add_field(name='Issue:', value=f'{ctx.message.author.mention}, you need to mention a member to unban them!')

            # Message sending
            await ctx.send(embed=embedVarA)

            # Printing to console
            print(f'{ctx.message.author} is missing required arguments')

    # Banlist command
    # Shows a list of banned users with Username, discriminator and ID
    @commands.command()
    @has_permissions(ban_members=True)
    async def banlist(self, ctx):

        """Check who is banned from the server!"""

        # Variables
        banned_users = await ctx.guild.bans()
        bans = ['• {0.name}#{0.discriminator} (ID: {0.id})'.format(entry.user) for entry in banned_users]

        # Checks if the list of banned users is empty
        if banned_users == []:

            # Design
            embedVar = discord.Embed(
                title='Ban list',
                description='List of users who are banned from this server.',
                colour=0x9f00ff
            )
            embedVar.add_field(name='Ban list', value='No one is banned')

            # Message sending
            await ctx.send(embed=embedVar)

            # Printing to console
            print('Banlist command used, no users are banned')

        # If the list of banned users is **not** empty 
        else:
            
            # Design
            embedVar = discord.Embed(
                title='Ban list:',
                description='List of users who are banned from this server.',
                colour=0xe74c3c
            )
            embedVar.add_field(name='Banned users:', value='\n'.join(bans))

            # Message sending
            await ctx.send(embed=embedVar)

            # Printing to console
            print('Banlist command used')

    # Banlist error handler
    @banlist.error
    async def banlist_error(self, ctx, error):

        # Checks if user is missing permissions
        if isinstance(error, MissingPermissions):

            # Design
            embedVar = discord.Embed(
                title='Insufficient Permission',
                description=f'{ctx.message.author.mention}, you do not have permission to perform this command',
                colour=0xe74c3c
            )
            embedVar.add_field(name='Issue', value='If you believe this is a mistake\nPlease contact a staff member')

            # Message sending
            await ctx.send(embed=embedVar)

            # Printing to console
            print(f'{ctx.message.author} is missing permission')

    # Mute command
    @commands.command()
    @has_permissions(manage_roles = True)
    async def mute(self, ctx, member: discord.Member, mute_minutes: int = 0, *, reason = None):

        """Use this to mute a user either permanently or temporarily."""

        # Finding the muted role
        muted = discord.utils.get(ctx.guild.roles, name = 'Muted')
        
        # Design
        embedVar = discord.Embed(
            title='Member muted',
            description=f'by {ctx.message.author.mention}',
            colour=0x9f00ff
        )
        embedVar.add_field(name='Member:', value=f'{member.mention}', inline=True)
        embedVar.add_field(name='Reason:', value=f'{reason}', inline=True)

        # Design depending on mute duration
        if mute_minutes == 0:
            embedVar.add_field(name='Duration:', value='Permanently muted', inline=True)
        else:
            embedVar.add_field(name='Duration:', value=f'{mute_minutes} seconds', inline=True)

        # Checking if the author has mentioned the bot
        if self.bot.user == member:
            embed = discord.Embed(title='You cannot mute me, I\'m an almighty bot!', colour=0xe74c3c)
            await ctx.send(embed=embed)

        # Checking whether the mentioned user is already muted
        if muted in member.roles:

            # Design
            embedVarM = discord.Embed(
                    title = 'Already muted',
                    description = f'{ctx.message.author.mention}, this user is already muted',
                    colour = 0xe74c3c
                )

            # Message sending
            await ctx.send(embed = embedVarM, delete_after = 15)

            # Printing to console
            print('Mute command used on already muted user')

        else:

            # Muting action - Adding the muted role to the mentioned user
            await member.add_roles(muted, reason = reason)

            # Message sending and deleting
            await ctx.send(embed = embedVar, delete_after = 15)
            await ctx.message.delete()

            # Printing to console
            print('Mute command used')
        
        # Checking if the mute duration is less than 0
        if mute_minutes > 0:
            await asyncio.sleep(mute_minutes)

            # Design
            embedVarE = discord.Embed(
                title='Unmuted',
                colour=0x9f00ff
            )
            embedVarE.add_field(name='Member unmuted:', value=f'{member.mention}', inline=True)
            embedVarE.add_field(name='Reason:', value='Mute time has been served', inline=True)

            # Automatic unmute action
            await member.remove_roles(muted, reason='Mute time has been served')

            # Message sending
            await ctx.send(embed=embedVarE)

            # Printing to console
            print(f'{member} has served their time')


    # Mute error handler
    @mute.error
    async def mute_error(self, ctx, error):

        # Checks if user is missing permissions
        if isinstance(error, MissingPermissions):

            # Design
            embedVarP = discord.Embed(
                title='Insufficient Permission',
                description=f'{ctx.message.author.mention}, you do not have permission to perform this command',
                colour=0xe74c3c
            )
            embedVarP.add_field(name='Issue:', value='If you believe this is a mistake\nPlease contact a staff member')

            # Message sending
            await ctx.send(embed=embedVarP)

            # Printing to console
            print(f'{ctx.message.author} is missing permission')

        # Checking if a user is mentioned
        if isinstance(error, commands.MissingRequiredArgument):

            # Design
            embedVarA = discord.Embed(
                title = 'Missing argument',
                description = f'{ctx.message.author.mention}, you need to mention a user!',
                colour = 0xe74c3c
            )

            # Message sending
            await ctx.send(embed = embedVarA)

            # Printing to console
            print(f'{ctx.message.author} is missing required arguments')

    # Unmute command
    @commands.command()
    @has_permissions(manage_roles = True)
    async def unmute(self, ctx, member: discord.Member):

        """Unmute a user!"""
        
        # Getting the role
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted')

        # Design
        embedVar = discord.Embed(
            title='Unmuted',
            description=f'by {ctx.message.author.mention}',
            colour=0x9f00ff
        )
        embedVar.add_field(name='Member:', value=f'{member.mention}, has been unmuted!')

        # Removing the role
        await member.remove_roles(muted_role, reason='Removed by Staff')

        # Message sending and deleting
        await ctx.send(embed=embedVar, delete_after=15)
        await ctx.message.delete()

        # Printing to console when used
        print('Unmute command used')

    # Unmute error handler
    @unmute.error
    async def unmute_error(self, ctx, error):

        # When the error is not having the permissions
        if isinstance(error, MissingPermissions):

            # Design
            embedVarP = discord.Embed(
                title='Insufficient Permission',
                description=f'{ctx.message.author.mention}, you do not have permission to perform this command',
                colour=0xe74c3c
            )
            embedVarP.add_field(name='Issue', value='If you believe this is a mistake\nPlease contact a staff member')

            # Message sending
            await ctx.send(embed=embedVarP)

        # When a user is not mentioned
        if isinstance(error, commands.MissingRequiredArgument):

            # Design
            embedVarA = discord.Embed(
                title='Missing Argument',
                colour=0xe74c3c
            )
            embedVarA.add_field(name='Issue:', value=f'{ctx.message.author.mention}, you need to mention a member to unmute them!')

            # Message sending
            await ctx.send(embed=embedVarA)

            # Printing to console
            print(f'{ctx.message.author} is missing required arguments')

# Adding the cog for main.py to access
def setup(bot):
    bot.add_cog(Moderation(bot))