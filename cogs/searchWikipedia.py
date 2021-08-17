import discord
from discord.ext import commands
import wikipedia


class SearchWikipedia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def search(self, ctx, query):
        result = wikipedia.summary(query, sentences=2)
        await ctx.send(result)


def setup(bot):
    bot.add_cog(SearchWikipedia(bot))
