import sys
import discord
from discord.ext import commands 
from helpers import getPrice
from helpers.manageacc import newaccount, exist
from helpers.save import save,load



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
    @commands.command(name="newacc")           
    async def newacc(self, ctx):
        print("\n\n\n"+str(str(ctx.author))+"\n\n\n")
        x = str(ctx.author)
        result = newaccount(x)
        await ctx.send(result)  
    @commands.command(name="buy")           
    async def buy(self, ctx, symbol, amount):
        x = str(ctx.author)
        if exist(x):
            user = load(x)
            result = user.buy(symbol.upper(),float(amount))
            save(user,x)
            await ctx.send(result) 
        else:
            await ctx.send("No account to buy with! enter: *newacc to create one")
    @commands.command(name="sell")           
    async def sell(self, ctx, symbol, amount):
        x = str(ctx.author)
        if exist(x):
            user = load(x)
            result = user.sell(symbol.upper(),float(amount))
            save(user,x)
            await ctx.send(result) 
        else:
            await ctx.send("No account to sell with.... Enter: *newacc to create one")
    @commands.command(name="balance")           
    async def balance(self, ctx):
        x = str(ctx.author)
        if exist(x):
            user = load(x)
            result = user.balance
            await ctx.send(result) 
        else:
            await ctx.send("No account... enter: *newacc to create one")
    @commands.command(name="coins")           
    async def coins(self, ctx):
        x = str(ctx.author)
        if exist(x):
            user = load(x)
            if user.coins:
                result = str(user.coins)
                await ctx.send(result[1:-1]) 
            else:
                await ctx.send("You haven't purchased any coins yet!")
        else:
            await ctx.send("No account... enter: *newacc to create one")
    @commands.command(name="portfolio")         
    async def portfolio(self, ctx):
        x = str(ctx.author)
        if exist(x):
            user = load(x)
            user.updatePortfolioPrice()
            result = user.portfolioValue
            await ctx.send(result) 
        else:
            await ctx.send("No account... enter: *newacc to create one")
def setup(bot):
    bot.add_cog(Crypto(bot))
    