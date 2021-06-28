# Made by Simoniezi

# Imports
import os
import sys
import traceback
from discord import activity
from dotenv import load_dotenv

import time

import random
from random import choice as randchoice

import discord
from discord import Member
from discord import embeds
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

import asyncio

# Intents
intents = discord.Intents.default()
intents.members = True


# Loading and finding Environmental Variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
BOT_OWNER_NAME = os.getenv('BOT_OWNER_NAME')
PREFIX = os.getenv('PREFIX')


# Stating my client
bot = commands.Bot(command_prefix = PREFIX)
bot.remove_command('help')


# Cogs
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_connect():
    
    # Telling when the bot is coonected to Discord
    print(f'{bot.user} has connected to Discord!')


# On Ready
@bot.event
async def on_ready():

    # Just a help for me, when I update it's activity
    # Could probably make a command out of it, but meh
    # Maybe I should though
    """
    Playing -> activity = discord.Game(name="!help")

    Streaming -> activity = discord.Streaming(name="!help", url="twitch_url_here")

    Listening -> activity = discord.Activity(type=discord.ActivityType.listening, name="!help")

    Watching -> activity = discord.Activity(type=discord.ActivityType.watching, name="!help")
    """

    # Defining the activity 
    activity = discord.Activity(
        type = discord.ActivityType.listening,
        name = '-c'
    )

    # Changing the bots presence
    await bot.change_presence(
        status=discord.Status.online,
        activity=activity
    )

    # Some Guild action
    # Was supposed to print the guilds that it's connected to, but it only works for 1 guild and not multiple smh
    GUILD = bot.guilds


    for guild in bot.guilds:
        if guild.name == GUILD:
            break


    print(
        f'Connected to the following guild(s):\n'
        f'{guild.name} (id: {guild.id})\n'
    )

# Responds to messages
# Allows everything to work, as it can actually pick up messages that is sent.
@bot.event
async def on_message(message):
    msg = message.content.casefold().capitalize()
    hello = ['Hello there!', 'Hiya!', 'Hiya', 'Good day!', 'Yo!', 'Yo', 'Hi', 'Hii', 'Hello', 'G\'day']

    helloRandom = randchoice(list(hello))

    if message.author == bot.user:
        return

    if msg in hello:
        print(f'Said hello: {helloRandom} \n')
        await message.channel.send(helloRandom)


    await bot.process_commands(message)

@bot.event
async def on_disconnect():
    print(f'{bot.user} has disconnected from Discord')

bot.run(TOKEN)