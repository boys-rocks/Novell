import discord
from discord.ext import commands
import requests


class GetWaifu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="waifu", help="Get yourself a Waifu.\nRequires a NSFW channel"
    )
    @commands.is_nsfw()
    async def get_waifu(self, ctx, query="waifu") -> None:
        """
        sends a random anime girl ( waifu ) image / gif

        :param query: type or action of/by waifu , defaults to "waifu"
        :type query: str, optional
        """
        with requests.get(url=f"https://api.waifu.pics/sfw/{query}") as response:
            try:
                await ctx.reply(response.json()["url"])
            except:
                await ctx.reply(
                    f"{query} is not a waifu type/action\n type: waifu neko shinobu megumin\n"
                    + "actions:  bully cuddle cry hug awoo kiss lick pat smug bonk yeet blush smile\n wave highfive handhold nom bite glomp slap kill kick happy wink poke dance cringe"
                )

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.NSFWChannelRequired):
            return await ctx.reply("not a NSFW CHANNEL.")


def setup(bot):
    bot.add_cog(GetWaifu(bot))
