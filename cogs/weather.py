import discord
from discord.ext import commands
from helpers.getWeather import getLocationKey, getWeather


class Weather(commands.Cog):
    """
    Weather Module
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Get Tempurature of Specified Location")
    async def weather(self, ctx, location):
        location_key = getLocationKey(location)
        location_temp = getWeather(location_key[0])
        await ctx.send(
            "The Tempurature of "
            + location
            + ", "
            + location_key[1]
            + " is "
            + str(location_temp[0])
            + "F,  "
            + str(location_temp[1])
            + "C"
        )


def setup(bot):
    bot.add_cog(Weather(bot))
