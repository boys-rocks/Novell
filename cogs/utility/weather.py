import discord
from discord.ext import commands
from helpers.getWeather import getWeather


class Weather(commands.Cog):
    """
    Weather Module
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Get Tempurature of Specified Location")
    async def weather(self, ctx, *, location: str) -> None:
        """
        displays weather details of a specified location

        :param location: specified location
        :type location: str
        """
        location_temp_f, location_temp_c = getWeather(location)
        await ctx.send(
            f"The tempurature of {location.title()} is {location_temp_f} F and {location_temp_c} C."
        )


def setup(bot):
    bot.add_cog(Weather(bot))
