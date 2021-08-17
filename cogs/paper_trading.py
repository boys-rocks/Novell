import sys
import discord
from discord.ext import commands 
from helpers import getPrice

class Crypto(commands.Cog):
    """
    Paper Trading Module
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help='Retrieve price data on specified cryptocurrency')
    async def price(self,ctx,symbol):
        currentPrice = getPrice.getPrice(symbol)
        if currentPrice:
            await ctx.send(f"The Current Price of {symbol} is {currentPrice}")
        else:
            await ctx.send("I'm having trouble finding that cryptocurrency, check for typos and try again :)")
    
def setup(bot):
    bot.add_cog(Crypto(bot))
    