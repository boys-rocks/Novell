import sys
import discord
from discord.ext import commands
from helpers import getPrice

from helpers.save import save, load, newaccount, exist


class Crypto(commands.Cog):
    """
    Paper Trading Module
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Retrieve price data on specified cryptocurrency")
    async def price(self, ctx, symbol):
        coin_and_price = getPrice.getPrice(symbol)
        if coin_and_price:
            await ctx.send(f"The Current Price of {symbol} is {coin_and_price[0]}")
        else:
            await ctx.send(
                "I'm having trouble finding that cryptocurrency, check for typos and try again :)"
            )

    @commands.command(name="newacc", help="Create new Papertrading acc")
    async def newacc(self, ctx):
        print("\n\n\n" + str(str(ctx.author)) + "\n\n\n")
        x = str(ctx.author)
        result = newaccount(x)
        await ctx.send(result)

    @commands.command(name="buy", help="Buy Crypto Currency")
    async def buy(self, ctx, symbol, amount):
        x = str(ctx.author)
        if exist(x):
            user = load(x)
            result = user.buy(symbol.upper(), float(amount))
            save(user, x)
            await ctx.send(result)
        else:
            await ctx.send("No account to buy with! enter: *newacc to create one")

    @commands.command(name="sell", help="Sell Crypto Currency")
    async def sell(self, ctx, symbol, amount):
        x = str(ctx.author)
        if exist(x):
            user = load(x)
            result = user.sell(symbol.upper(), float(amount))
            save(user, x)
            await ctx.send(result)
        else:
            await ctx.send("No account to sell with.... Enter: *newacc to create one")

    @commands.command(name="balance", help="Get cash balance of paper trading account")
    async def balance(self, ctx):
        x = str(ctx.author)
        if exist(x):
            user = load(x)
            result = user.balance
            await ctx.send(result)
        else:
            await ctx.send("No account... enter: *newacc to create one")

    @commands.command(name="coins", help="Get list of coins you have")
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

    @commands.command(name="portfolio", help="Get value of portfolio")
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
