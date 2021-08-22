import discord
from discord.ext import commands


class Calculator(commands.Cog):
    "Calculator Module"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Calculator command")
    async def clc(self, ctx, *query):
        problem = " ".join(query)
        result = eval(problem)
        await ctx.send(f"```{problem} = {result}```")


def setup(bot):
    bot.add_cog(Calculator(bot))
