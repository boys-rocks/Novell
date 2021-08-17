import discord
from discord.ext import commands
import requests


class Jokes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        try:
            x = requests.get('https://official-joke-api.appspot.com/random_joke')
            await ctx.send(x.json()['setup'])
            await ctx.send(x.json()['punchline'])
        except Exception as ex:
            print('Exception', ex)

    @commands.command()
    async def affirm(self, ctx):
        try:
            x = requests.get('https://www.affirmations.dev/')
            await ctx.send(x.json()['affirmation'])
        except Exception as ex:
            print('Exception: ', ex)

def setup(bot):
    bot.add_cog(Jokes(bot))
