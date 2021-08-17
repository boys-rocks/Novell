import discord
from discord.ext import commands
import requests


class ProgrammingJoke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def projoke(self, ctx):
        with requests.get(
                url=f"https://v2.jokeapi.dev/joke/programming?type=single"
        ) as response:
            await ctx.send(response.json()['joke'])


def setup(bot):
    bot.add_cog(ProgrammingJoke(bot))
