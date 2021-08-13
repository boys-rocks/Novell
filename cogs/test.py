import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cogstest(self,ctx):
        await ctx.send('Cogs working.')

def setup(bot):
    bot.add_cog(Test(bot))