import discord
from discord.ext import commands


class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clc(self, ctx, query):
        result = eval(query)
        await ctx.send(f"```{query} = {result}```")


def setup(bot):
    bot.add_cog(Calculator(bot))
