# Made by Simoniezi

# Imports
import random
from random import choice as randchoice

import discord
from discord import Member
from discord import embeds
from discord.ext import commands
from discord.ext.commands import CommandOnCooldown

# Fun handler
class Fun(commands.Cog):

    """
    All the fun and game commands
    """

    # Initialising the script
    def __init__(self, bot):
        self.bot = bot

    # Prints to console when ready
    @commands.Cog.listener()
    async def on_ready(self):
        print('FunHandler is ready')

    # Ping command
    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def ping(self, ctx):

        """Your standard ping command"""

        # Design
        embedVar = discord.Embed(
            colour=0x9f00ff
        )
        embedVar.add_field(name='Pong!', value=f'{round(self.bot.latency * 1000)}ms')

        # Message sending
        await ctx.send(embed=embedVar)

        # Printing to console
        print('Ping command used')
        print(round(self.bot.latency * 1000))

    # Ping error handler
    @ping.error
    async def ping_error(self, ctx, error):

        # Checking if the command is on cooldown
        if isinstance(error, commands.CommandOnCooldown):

            # Design
            embedVarC = discord.Embed(
                title='On cooldown!',
                description=f'{ctx.message.author.mention}, you have to wait 30 seconds from last use!',
                colour=0xe74c3c
            )

            # Message sending
            await ctx.send(embed=embedVarC, delete_after=10)

    # 8ball command
    @commands.command(aliases=['8ball'])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def _8ball(self, ctx, *, question):

        """Ask the 8ball anything! (the '_' is not needed in the command)"""

        # Responses available
        responses = [
            'It is decidedly so.',
            'Without a doubt!',
            'Yes - definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',
            'Reply hazy, try again.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don\'t count on it.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Very doubtful.'
        ]

        # Design
        embedVar = discord.Embed(title='8Ball', colour=0x9f00ff)
        embedVar.add_field(name='**Question:**', value=f'{question}', inline=False)
        embedVar.add_field(name='**Answer:**', value=f'{random.choice(responses)}', inline=False)

        # Message sending
        await ctx.send(embed=embedVar)
       
        # Printing to console
        print('8ball command used')

    # 8ball error handler
    @_8ball.error
    async def _8ball_error(self, ctx, error):

        # Checking if there is no argument (In this case, a question)
        if isinstance(error, commands.MissingRequiredArgument):

            # Design
            embedVarRA = discord.Embed(
                title='Missing Argument',
                colour=0xe74c3c
            )
            embedVarRA.add_field(name='Issue:', value=f'{ctx.message.author.mention}, you need to provide me a question I can answer!')

            # Message sending
            await ctx.send(embed=embedVarRA)

        # Checking if the command is on cooldown
        if isinstance(error, commands.CommandOnCooldown):

            # Design
            embedVarC = discord.Embed(
                title='On cooldown!',
                description=f'{ctx.message.author.mention}, you have to wait 30 seconds from last use!',
                colour=0xe74c3c
            )

            # Message sending
            await ctx.send(embed=embedVarC, delete_after=10)

    # Rock-paper-scissors command
    @commands.command()
    async def rps(self, ctx, choice : str):

        """Play rock-paper-scissors!"""

        # Variables and bot choice code
        author = ctx.message.author
        rpsbot = {"rock" : ":moyai:",
           "paper": ":page_facing_up:",
           "scissors":":scissors:"}
        choice = choice.lower()
        if choice in rpsbot.keys():
            print('RPS command used')
            botchoice = randchoice(list(rpsbot.keys()))
            msgs = {
                "win": " You win {}!".format(author.mention),
                "square": " We're square {}!".format(author.mention),
                "lose": " You lose {}!".format(author.mention)
            }

            # The win and lose mechanic
            if choice == botchoice:
                await ctx.send(rpsbot[botchoice] + msgs["square"])
            elif choice == "rock" and botchoice == "paper":
                await ctx.send(rpsbot[botchoice] + msgs["lose"])
            elif choice == "rock" and botchoice == "scissors":
                await ctx.send(rpsbot[botchoice] + msgs["win"])
            elif choice == "paper" and botchoice == "rock":
                await ctx.send(rpsbot[botchoice] + msgs["win"])
            elif choice == "paper" and botchoice == "scissors":
                await ctx.send(rpsbot[botchoice] + msgs["lose"])
            elif choice == "scissors" and botchoice == "rock":
                await ctx.send(rpsbot[botchoice] + msgs["lose"])
            elif choice == "scissors" and botchoice == "paper":
                await ctx.send(rpsbot[botchoice] + msgs["win"])
        else:
            await ("Choose rock, paper or scissors.")

        # Printing to console
        print(botchoice.capitalize())

    # Rock-paper-scissors error handler
    @rps.error
    async def rps_error(self, ctx, error):

        # Checks if there is a missing argument
        if isinstance(error, commands.MissingRequiredArgument):

            # Design
            embedVar = discord.Embed(
                title='Missing Argument',
                colour=0xe74c3c
            )
            embedVar.add_field(name='Issue:', value=f'{ctx.message.author.mention}, you need to choose between rock, paper or scissors!')

            # Message sending
            await ctx.send(embed=embedVar)

    # Coinflip command
    @commands.command()
    async def flip(self, ctx, choice: str):

        """Your standard coinflip!"""

        # Variables
        coin =['heads', 'tails']

        choice = choice.lower()
        coinflip = randchoice(list(coin))

        # The game mechanics
        if coinflip == 'heads':
            if choice == coinflip:
                embedVarHW = discord.Embed(
                    title='It\'s heads!',
                    description='You win!',
                    colour=0x9f00ff
                )
                embedVarHW.set_image(url='https://i.colnect.net/f/3429/404/20-Kroner-LG-JP-A.jpg')
                await ctx.send(embed=embedVarHW)
            else:
                embedVarHL = discord.Embed(
                    title='It\'s heads!',
                    description='You lose!',
                    colour=0x9f00ff
                )
                embedVarHL.set_image(url='https://i.colnect.net/f/3429/404/20-Kroner-LG-JP-A.jpg')
                await ctx.send(embed=embedVarHL)
        elif coinflip == 'tails':
            if choice == coinflip:
                embedVarTW = discord.Embed(
                    title='It\'s tails!',
                    description='You win!',
                    colour=0x9f00ff
                )
                embedVarTW.set_image(url='https://i.colnect.net/b/3429/415/20-Kroner-LG-JP-A-back.jpg')
                await ctx.send(embed=embedVarTW)
            else:
                embedVarTL = discord.Embed(
                    title='It\'s tails!',
                    description='You lose!',
                    colour=0x9f00ff
                )
                embedVarTL.set_image(url='https://i.colnect.net/b/3429/415/20-Kroner-LG-JP-A-back.jpg')
                await ctx.send(embed=embedVarTL)
        
        # Printing to console
        print('Flip command used')
        print(coinflip)

    # Coinflip error handler
    @flip.error
    async def flip_error(self, ctx, error):

        # Checking if there an argument is missing
        if isinstance(error, commands.MissingRequiredArgument):

            # Design
            embedVar = discord.Embed(
                title='Missing Arguments',
                colour=0xe74c3c
            )
            embedVar.add_field(name='Issue:', value=f'{ctx.message.author.mention}, you need to choose either heads or tails!')

            # Message sending
            await ctx.send(embed=embedVar)

        # Checking if it is a bad argument - an argument unusable for the game
        if isinstance(error, commands.BadArgument):

            # Design
            embedVar = discord.Embed(
                title='Bad Arguments',
                colour=0xe74c3c
            )
            embedVar.add_field(name='Issue:', value=f'{ctx.message.author.mention}, you need to choose either heads or tails!')

            # Message sending
            await ctx.send(embed=embedVar)

    # Repeat/copy/say command
    @commands.command(name='repeat', aliases=['mimic', 'copy', 'say'])
    async def do_repeat(self, ctx, *, inp: str):

        """This is a command where you can make the bot say things!"""

        # Message sending
        # Here we are taking the user input and making it send that and delete the user message
        await ctx.send(inp)
        await ctx.message.delete()

        # Printing to console
        # Printing the user input message just for safety, if anything should happen
        print('Repeat command used')
        print(f'{ctx.message.content}')


    # Repeat/copy/say error handler
    @do_repeat.error
    async def do_repeat_handler(self, ctx, error):

        # Checking if there is a missing argument
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'inp':
                await ctx.send('You forgot to give me an input to repeat!')



# Adding the cog for main.py to access
def setup(bot):
    bot.add_cog(Fun(bot))