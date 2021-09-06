import discord
from discord.ext import commands
import requests


class GetWaifu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="waifu", help="Get yourself a Waifu.")
    async def get_waifu(self, ctx, query="waifu"):
        with requests.get(url=f"https://api.waifu.pics/sfw/{query}") as response:
            if response.status_code == 200:
                try:
                    await ctx.reply(response.json()["url"])
                except:
                    await ctx.reply(
                        f"{query} don't wanna be your waifu. Try something else."
                    )
            else:
                await ctx.send("API is down")


def setup(bot):
    bot.add_cog(GetWaifu(bot))
