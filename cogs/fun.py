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
        await ctx.send(embed=discord.Embed(title=x.json()['activity'], description=x.json()['type'])

    @commands.command(help='Predict which country a name is from')
    async def name(self, ctx, *, name):
        y = requests.get(f'https://api.nationalize.io?name={name}')
        await ctx.send(f'Your name is likely from {y.json()['country'][0]['country_id']}')

def setup(bot):
    bot.add_cog(Fun(bot))

