# Third party libraries
import discord
from discord.ext import commands
from random import choice
import string


class PasswordGenerator(commands.Cog):

    """
    Generates a password from unicode decimal ranges.
    """

    def __init__(self, bot):  # Initialize cog.

        self.bot = bot

    @commands.command(help="Generates strong password")
    async def getpassword(self, ctx, query=15):
        characters = string.ascii_letters + string.punctuation + string.digits
        password = "".join(choice(characters) for x in range(query))
        await ctx.author.send(
            f"```Disclaimer: We are not responsible for compromised accounts. \n\nPassword: {password}```"
        )


# Standard cog setup.
def setup(bot):
    bot.add_cog(PasswordGenerator(bot))
