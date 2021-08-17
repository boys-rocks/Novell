import discord
from discord.ext import commands
import requests


class ChuckJokes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chuckjokes(self, ctx):
        with requests.get(
                url=f"http://api.icndb.com/jokes/random") as response:
            await ctx.send(response.json()['value']['joke'])


def setup(bot):
    bot.add_cog(ChuckJokes(bot))
