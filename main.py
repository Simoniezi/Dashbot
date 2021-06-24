# Made by Simoniezi

# Imports
import os
import sys
import traceback
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


# Main Code
@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game('-c || Working very hard!')
    )

    print(f'{bot.user} has connected to Discord!')

    GUILD = bot.guilds


    for guild in bot.guilds:
        if guild.name == GUILD:
            break


    print(
        f'Connected to the following guild(s):\n'
        f'{guild.name} (id: {guild.id})\n'
    )


@bot.event
async def on_message(message):
    msg = message.content.casefold().capitalize()
    hello = ['Hello there!', 'Hiya!', 'Hiya', 'Good day!', 'Yo!', 'Yo', 'Hi', 'Hii', 'Hello', 'G\'day']
    #helloYuwu = ['Hello yuwu!', 'Hi yuwu!', 'Hihi yuwu!', 'Hiya yuwu!']

    helloRandom = randchoice(list(hello))
  #  helloYuwuRandom = randchoice(list(helloYuwu))

    if message.author == bot.user:
        return

    if msg in hello:
        print('Said hello')
        #  if str(message.author) == 'Simoniezi#7138':
            #   await message.channel.send('Hi owner!')
    #  elif str(message.author) == 'yuru says desu#7082':
    #     await message.channel.send(helloYuwuRandom)
    #       time.sleep(30)
        #else:
        await message.channel.send(helloRandom)


    await bot.process_commands(message)

bot.run(TOKEN)