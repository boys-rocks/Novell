import logging
import discord
from discord.ext import commands
import requests


class Madlibs(commands.Cog):
    """Mad Libs is a phrasal template word game created by Leonard Stern and Roger Price."""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(help="starts Madlibs game")
    async def madlibs(self, ctx, maxlength=None):
        try:
            if maxlength is None or int(maxlength) < 5:
                maxlength = 6
        except Exception as error:
            await ctx.send("Invalid max length")
            logging.warning(f"madlibs: {error}")
            return
        with requests.get(
            "http://madlibz.herokuapp.com/api/random?minlength=5&maxlength={maxlength}"
        ) as response:
            user_repsonses = {}
            all_blanks = response.json()["blanks"]
            for blank in all_blanks:
                await ctx.send(f"enter a/an {blank}:  ")
                usr_rsp = await self.bot.wait_for(
                    "message", check=lambda message: message.author == ctx.author
                )
                user_repsonses[blank] = usr_rsp
            combined_respose = zip(user_repsonses, response.json()["value"])
            await ctx.reply(
                response.json()["title"]
                + "\n"
                + " ".join([" ".join(i) for i in combined_respose])
            )


def setup(bot):
    bot.add_cog(Madlibs(bot))
