import discord
from discord.ext import commands
from random import choice

from requests.models import Response


class Choose(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def toss(self, ctx):
        await ctx.send(f"Coin is tossed, and.... it's {choice(['HEADS','TAILS'])}")

    @commands.command()
    async def choose(self, ctx, *args):
        respose = choice(
            ["choose", "prefer", "think you should go with", "would choose"]
        )
        await ctx.send(f"Well! , I {respose} {choice(args)}")


def setup(bot):
    bot.add_cog(Choose(bot))
