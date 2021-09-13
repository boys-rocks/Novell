import discord
from discord.ext import commands


class StandUp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command for setting message time

    # Command for adding users to message list

    # main function for going through questions
    #  for each user added to the standup list, send a pm message for the questions
    #

    # On message event, listen for user response to append to image


def setup(bot):
    bot.add_cog(StandUp(bot))
