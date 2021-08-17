import discord
from discord.ext import commands
import requests


class Bored(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bored(self, ctx):
        with requests.get(
                url=f"http://www.boredapi.com/api/activity/") as response:
            link = ""
            try:
                link = response.json()["link"]
            except:
                link = "none"

            await ctx.send(
                f"``activity: {response.json()['activity']}\ntype:{response.json()['type']}\nlink: {link}``"
            )


def setup(bot):
    bot.add_cog(Bored(bot))
