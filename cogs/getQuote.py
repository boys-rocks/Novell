import discord
import requests
from discord.ext import commands


def fetch_quote():
    response = requests.get(url="https://animechan.vercel.app/api/random")
    anime_name = response.json()["anime"]
    character_name = response.json()["character"]
    character_quote = response.json()["quote"]
    return f"``{character_quote}``\n - {character_name}\n - {anime_name} "


class GetQuote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def inspire_me(self, ctx):
        await ctx.send(fetch_quote())


def setup(bot):
    bot.add_cog(GetQuote(bot))
