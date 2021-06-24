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

    @commands.command(aliases=['ar'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    @has_permissions(manage_roles = True)
    async def addrole(self, ctx, member: discord.Member, roles: discord.guild.Role):
        await member.add_roles(roles)
        await ctx.send('Role added to user')

    @addrole.error
    async def addrole_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send('You don\'t have permission to perform this command!')

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send('You have to wait 10 seconds for the cooldown to end!')

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You have to mention a user!')

    @commands.command(aliases=['rr'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    @has_permissions(manage_roles = True)
    async def removerole(self, ctx, member: discord.Member, roles: discord.guild.Role):
        await member.remove_roles(roles)
        await ctx.send('Role removed from user')

    @removerole.error
    async def removeroles_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send('You don\'t have permission to perform this command!')

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send('You have to wait 10 seconds for the cooldown to end!')

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You have to mention a user!')

def setup(bot):
    bot.add_cog(Config(bot))
