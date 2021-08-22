import discord
from discord.ext import commands
import requests
import os

# OWL_BOT_TOKEN = os.environ.get("OWL_BOT_TOKEN")
OWL_BOT_TOKEN = "64154ef64d2de67c9f031ac98798fb57eaaf2f41"
HEADER = {"Authorization": OWL_BOT_TOKEN}


class Dictionary(commands.Cog):
    """
    Dictionary Module
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Get word definitions")
    async def dictionary(self, ctx, word):
        with requests.get(
            url=f"https://owlbot.info/api/v4/dictionary/{word}/",
            headers={"Authorization": "Token 64154ef64d2de67c9f031ac98798fb57eaaf2f41"},
        ) as response:
            rsp = response.json()
            await ctx.send(
                f"```word: {rsp['word']}\ndefinition: {rsp['definitions'][0]['definition']}```"
            )
            try:
                await ctx.send(response.json()["definitions"][0]["image_url"])

            except:
                print("no image available")


def setup(bot):
    bot.add_cog(Dictionary(bot))
