import string
from random import choice
import discord
from discord.ext import commands


class GetPassword(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def getpassword(self, ctx, query=15):
        characters = string.ascii_letters + string.punctuation + string.digits
        password = "".join(choice(characters) for x in range(query))
        await ctx.author.send(
            f"```Disclaimer: We are not responsible for compromised accounts. \n\nPassword: {password}```"
        )


def setup(bot):
    bot.add_cog(GetPassword(bot))
