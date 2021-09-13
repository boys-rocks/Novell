import logging
import discord
from discord.ext import commands
import requests


class Madlibs(commands.Cog):
    """Mad Libs is a phrasal template word game created by Leonard Stern and Roger Price."""

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(help="play Madlibs game")
    async def madlibs(self, ctx, maxlength: int = None) -> None:
        """
        starts madlib game

        :param maxlength: max number of blanks, defaults to None
        :type maxlength: int, optional
        """
        try:
            if maxlength is None or int(maxlength) < 5:
                maxlength = 10
        except Exception as error:
            await ctx.send("Invalid max length")
            logging.warning(f"madlibs: {error}")
            return
        with requests.get(
            "http://madlibz.herokuapp.com/api/random?minlength=5&maxlength={maxlength}"
        ) as response:
            if response.status_code == 200:
                user_repsonses = {}
                all_blanks = response.json()["blanks"]
                for blank in all_blanks:
                    await ctx.send(f"enter a/an {blank}:  ")
                    usr_rsp = await self.bot.wait_for(
                        "message", check=lambda message: message.author == ctx.author
                    )
                    user_repsonses[blank] = usr_rsp.content.upper()
                combined_respose = zip(
                    response.json()["value"], user_repsonses.values()
                )
                await ctx.reply(
                    response.json()["title"]
                    + "\n"
                    + " ".join([" ".join(i) for i in combined_respose])
                )
            else:
                await ctx.send("API is not working.")


def setup(bot):
    bot.add_cog(Madlibs(bot))
