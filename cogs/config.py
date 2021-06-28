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

# Environmental Variables
load_dotenv()

BOT_OWNER_NAME = os.getenv('BOT_OWNER_NAME')

# Config handler
class Config(commands.Cog):

    """
    All the essential configuration commands
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('ConfigHandler is ready!')

    # Invite command
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def invite(self, ctx):

        """
        You're basic bot invite command
        """

        # Design
        embedVar = discord.Embed(
            title='Invite!',
            description=f'Add this bot to your own server!',
            colour=0x9f00ff
        )
        inviteLink = 'https://discord.com/api/oauth2/authorize?client_id=789152861484744704&permissions=0&scope=bot'
        embedVar.set_author(name='Simoniezi', icon_url='https://pbs.twimg.com/profile_images/1280541344834994176/tBkIGV1S_400x400.jpg')
        embedVar.add_field(name='Link', value=f'[Invite it here!]({inviteLink})')
        embedVar.set_footer(text=f'This bot is run and owned by {BOT_OWNER_NAME}')

        # Message sending
        await ctx.send(embed=embedVar)

        # Printing to console
        print('Invite command was used')

    @invite.error
    async def invite_error(self, ctx, error):
        # Checking if the command is on cooldown
        if isinstance(error, commands.CommandOnCooldown):

            # Design
            embedVarC = discord.Embed(
                title='On cooldown!',
                description=f'{ctx.message.author.mention}, you have to wait 10 seconds from last use!',
                colour = 0xe74c3c
            )

            # Message sending
            await ctx.send(embed=embedVarC, delete_after=10)

    # Add role command
    # Requires the manage_roles permission
    @commands.command(aliases=['ar'])
    @has_permissions(manage_roles = True)
    async def addrole(self, ctx, member: discord.Member, roles: discord.guild.Role):

        """
        A simple role adding command.
        Remember to check capitalisation when writing the role.
        """

        # Checks if the mentioned member has the role or not
        if roles in member.roles:
            
            # Design
            embedVarHR = discord.Embed(
                title = 'Has role',
                colour = 0xe74c3c
            )
            embedVarHR.add_field(
                name = 'Issue',
                value = f'{ctx.message.author.mention}, this member already has this role'
            )

            # Message sending
            await ctx.send(embed = embedVarHR)

            # Printing to console
            print(f'{ctx.message.author} tried to add a role, which {member} already has')

        else:

            # Design
            embedVarAR = discord.Embed(
                title = 'Role added!',
                description = f'by {ctx.message.author.mention}',
                colour = 0x9f00ff
            )
            embedVarAR.add_field(
                name = 'Member', 
                value = f'{member.mention}', 
                inline = True
            )
            embedVarAR.add_field(
                name = 'Role',
                value = f'{roles.mention}',
                inline = True
            )

            # Adding the mentioned role to the mentioned user
            await member.add_roles(roles)

            # Message sending
            await ctx.send(embed=embedVarAR)

            # Printing to console
            print('Add roles command used')

    # Add role error handler
    @addrole.error
    async def addrole_error(self, ctx, error):

        # Checking if the user is missing permission
        if isinstance(error, MissingPermissions):

            # Design
            embedVarMP = discord.Embed(
                title = 'Missing Permission',
                description=f'{ctx.message.author.mention}, you do not have permission to perform this command',
                colour = 0xe74c3c
            )
            embedVarMP.add_field(
                name = 'Issue', 
                value='If you believe this is a mistake\nPlease contact a staff member'
            )

            # Message sending
            await ctx.send(embed=embedVarMP)

            # Printing to console
            print(f'{ctx.message.author} is missing permission to perform add role')

        # Checking if the command is on cooldown
        """
        if isinstance(error, commands.CommandOnCooldown):

            # Design
            embedVarC = discord.Embed(
                title = 'On Cooldown',
                description = f'{ctx.message.author.mention}, this command is on cooldown!',
                colour = 0xe74c3c
            )
            embedVarC.add_field(
                name = 'Cooldown',
                
                # This tells how much time is left
                value = 'Try again in {:.2f}s'.format(error.retry_after)
            )

            # Message sending
            await ctx.send(embed=embedVarC)

            # Printing to console
            print('Add roles command is on cooldown \n {:.2f}s is left \n'.format(error.retry_after))
        """

        # Checks if a user is mentioned
        if isinstance(error, commands.MissingRequiredArgument):

            # Design
            embedVarRA = discord.Embed(
                title = 'Missing Argument',
                description = f'{ctx.message.author.mention}, you need to mention a user!',
                colour = 0xe74c3c
            )

            # Message sending
            await ctx.send(embed = embedVarRA)

            # Printing to console
            print(f'{ctx.message.author} is missing required arguements')

        # Checks if the user has given a proper arguement
        if isinstance(error, commands.BadArgument):

            # Design
            embedVarBA = discord.Embed(
                title= 'Bad Argument',
                description = f'{ctx.message.author.mention}, you need to provide a proper role (Check capitalisation)',
                colour = 0xe74c3c
            )

            # Message sending
            await ctx.send(embed = embedVarBA)

            # Printing to console
            print(f'{ctx.message.author} provided a bad arguement')

    # Remove role command
    # Requires the manage_roles permission
    @commands.command(aliases=['rr'])
    @has_permissions(manage_roles = True)
    async def removerole(self, ctx, member: discord.Member, roles: discord.guild.Role):

        """
        A simple role removing command.
        Remember to check capitalisation when writing the role.
        """

        # Checks if the mentioned user has the mentioned role
        if roles not in member.roles:
            
            # Design
            embedVarNRR = discord.Embed(
                title = 'Does not have the role',
                colour = 0xe74c3c
            )
            embedVarNRR.add_field(
                name = 'Issue',
                value = f'{ctx.message.author.mention}, this member does not have this role',
                inline = True
            )

            # Message sending
            await ctx.send(embed = embedVarNRR)

            # Printing to console
            print(f'{ctx.message.author} tried to remove a role from {member}, which they did not have')

        else:

            # Design
            embedVarRR = discord.Embed(
                title = 'Removed role',
                description = f'by {ctx.message.author.mention}',
                colour = 0x9f00ff
            )
            embedVarRR.add_field(
                name = 'Member',
                value = f'{member.mention}',
                inline = True
            )
            embedVarRR.add_field(
                name = 'Role',
                value = f'{roles.mention}',
                inline = True
            )

            # Command action
            await member.remove_roles(roles)

            # Message sending
            await ctx.send(embed = embedVarRR)

            # Printing to console
            print('Remove role command used')

    # Remove role error handler
    @removerole.error
    async def removeroles_error(self, ctx, error):

        # Checks if the user is missing permission
        if isinstance(error, MissingPermissions):

            # Design
            embedVarMP = discord.Embed(
                title = 'Missing Permission',
                description=f'{ctx.message.author.mention}, you do not have permission to perform this command',
                colour = 0xe74c3c
            )
            embedVarMP.add_field(
                name = 'Issue', 
                value='If you believe this is a mistake\nPlease contact a staff member'
            )

            # Message sending
            await ctx.send(embed = embedVarMP)

            # Printing to console
            print(f'{ctx.message.author} is missing permission to perform remove role')

        # Checks if command is on cooldown
        """
        if isinstance(error, commands.CommandOnCooldown):
            
            # Design
            embedVarC = discord.Embed(
                title = 'On Cooldown',
                description = f'{ctx.message.author.mention}, this command is on cooldown!',
                colour = 0xe74c3c
            )
            embedVarC.add_field(
                name = 'Cooldown',
                
                # This tells how much time is left
                value = 'Try again in {:.2f}s'.format(error.retry_after)
            )

            # Message sending
            await ctx.send(embed=embedVarC)

            # Printing to console
            print('Remove roles command is on cooldown \n {:.2f}s is left \n'.format(error.retry_after))

        """

        # Checks if a user is mentioned
        if isinstance(error, commands.MissingRequiredArgument):
           
            # Design
            embedVarRA = discord.Embed(
                title = 'Missing Argument',
                description = f'{ctx.message.author.mention}, you need to mention a user!',
                colour = 0xe74c3c
            )

            # Message sending
            await ctx.send(embed = embedVarRA)

            # Printing to console
            print(f'{ctx.message.author} is missing required arguements')

        # Checks if the user has given a proper arguement
        if isinstance(error, commands.BadArgument):

            # Design
            embedVarBA = discord.Embed(
                title= 'Bad Argument',
                description = f'{ctx.message.author.mention}, you need to provide a proper role (Check capitalisation)',
                colour = 0xe74c3c
            )

            # Message sending
            await ctx.send(embed = embedVarBA)

            # Printing to console
            print(f'{ctx.message.author} provided a bad arguement')

# Adding the cog for main.py to access
def setup(bot):
    bot.add_cog(Config(bot))