import discord
from discord.ext import commands
import requests

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help='Get an activity')
    async def activity(self, ctx):
        import requests
        x = requests.get("https://www.boredapi.com/api/activity")
        await ctx.send(embed=discord.Embed(title=x.json()['activity'], description=x.json()['type']))

def setup(bot):
    bot.add_cog(Fun(bot))

