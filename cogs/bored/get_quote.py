import discord
import requests
from discord.ext import commands


def fetch_quote() -> str:
    """
    gets a random anime quote

    param return: return a quote
    type return: str
    """
    response = requests.get(url="https://animechan.vercel.app/api/random")
    anime_name = response.json()["anime"]
    character_name = response.json()["character"]
    character_quote = response.json()["quote"]
    return f"```{character_quote}\n -- {character_name} [ {anime_name} ] ```"


class GetQuote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Retrieves a random anime quote")
    async def quote(self, ctx) -> None:
        """
        sends a random anime quote

        """
        try:
            await ctx.send(fetch_quote())
        except Exception as error:
            await ctx.send(f"something went wrong\n")


def setup(bot):
    bot.add_cog(GetQuote(bot))
