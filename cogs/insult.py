import discord
from discord.ext import commands
import requests


class ThrowInsult(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def insult(self, ctx):
        with requests.get(
            url=f"https://evilinsult.com/generate_insult.php?lang=en&type=json"
        ) as response:
            await ctx.send(response.json()["insult"])


def setup(bot):
    bot.add_cog(ThrowInsult(bot))
