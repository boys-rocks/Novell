import discord
from discord.ext import commands
import requests


class GetWaifu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="waifu", help="Get yourself a Waifu.")
    @commands.is_nsfw()
    async def get_waifu(self, ctx, query="waifu"):
        with requests.get(url=f"https://api.waifu.pics/sfw/{query}") as response:
            try:
                await ctx.reply(response.json()["url"])
            except:
                await ctx.reply(
                    f"{query} don't wanna be your waifu. Try something else."
                )

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.NSFWChannelRequired):
            return await ctx.reply("not a NSFW CHANNEL.")


def setup(bot):
    bot.add_cog(GetWaifu(bot))
