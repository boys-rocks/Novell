import discord
from discord.ext import commands
import requests


class Madlibs(commands.Cog):
    """Mad Libs is a phrasal template word game created by Leonard Stern and Roger Price."""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(help="starts Madlibs game")
    async def madlibs(self, ctx, maxlength=None):
        if maxlength is None or maxlength < 5:
            maxlength = 8
        with requests.get(
            "http://madlibz.herokuapp.com/api/random?minlength=5&maxlength={maxlength}"
        ) as response:
            user_repsonse = {}
            all_blanks = response.json()["blanks"]
            for blank in all_blanks:
                await ctx.send(f"enter a/an {blank}:  ")
                response = await self.bot.wait_for(
                    "message", check=lambda message: message.author == ctx.author
                )
                user_repsonse[blank] = response
            combined_respose = zip(user_repsonse, response.json()["value"])
            await ctx.reply(
                response.json()["title"]
                + "\n"
                + " ".join([" ".join(i) for i in combined_respose])
            )


def setup(bot):
    bot.add_cog(Madlibs(bot))
