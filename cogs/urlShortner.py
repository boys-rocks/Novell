import discord
from discord.ext import commands
import requests


def shortner(url):
    with requests.get(
        f"https://cutt.ly/api/api.php?key=18e866ec48230e692db0f4a225c72fcabfb1e&short={url}"
    ) as response:
        return f"{response.json()['url']['shortLink']}"


class UrlShortner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shrink(self, ctx, full_url):

        await ctx.send(f"```shortened link:\n {shortner(full_url)}```")


def setup(bot):
    bot.add_cog(UrlShortner(bot))
