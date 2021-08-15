import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(help='Checks if Cogs are working')
    async def cogstest(self,ctx):
        await ctx.send('Cogs working.')
    @commands.command(help='Check Latency')
    async def ping(self,ctx):
        em = discord.Embed(title='Pong!', description=str(round(self.bot.latency * 1000)) + 'ms')
        await ctx.send(embed=em)
def setup(bot):
    bot.add_cog(Test(bot))