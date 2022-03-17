import discord
from discord.ext import commands
import requests
import os

OWL_BOT_TOKEN = os.environ.get("OWL_BOT_TOKEN")
HEADER = {"Authorization": OWL_BOT_TOKEN}


class Dictionary(commands.Cog):
    """
    Dictionary Module
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Get word definitions")
    async def dictionary(self, ctx, word: str) -> None:
        """
        Search the word in dictionary and sends its meaning to user

        :param word: word to search for
        :type word: str
        """
        with requests.get(
            url=f"https://owlbot.info/api/v4/dictionary/{word}/",
            headers={"Authorization": "Token 64154ef64d2de67c9f031ac98798fb57eaaf2f41"},
        ) as response:
            rsp = response.json()
            try:
                em = discord.Embed(
                    title=rsp["word"],
                    description=f'{rsp["definitions"][0]["definition"]}\nExample: {rsp["definitions"][0]["example"]}'
                )
                await ctx.send(em)
                # await ctx.send(
                #     f"```word: {rsp['word']}\ndefinition: {rsp['definitions'][0]['definition']}```"
                # )
                # if response.json()["definitions"][0]["image_url"]:
                #     await ctx.send(response.json()["definitions"][0]["image_url"])
            except Exception as error:
                await ctx.send("API down")


def setup(bot):
    bot.add_cog(Dictionary(bot))
