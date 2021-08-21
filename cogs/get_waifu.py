import discord
from discord.ext import commands
import requests





class GetWaifu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
        
        
        

    @commands.command()
    async def waifu(self, ctx, query):
        with requests.get(url=f"https://api.waifu.pics/sfw/{query}") as response:
            try:
                
                
                
                
                await ctx.send(response.json()["url"])
                
                
                
                
                
            except:
                
                
                
                
                await ctx.send("Looks like no one likes you")


def setup(bot):
    bot.add_cog(GetWaifu(bot))
