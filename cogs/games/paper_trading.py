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
    async def price(self, ctx, symbol: str) -> None:
        """
        get price for the requested currency

        :param symbol: currency symbol
        :type symbol: str
        """
        coin_and_price = getPrice.getPrice(symbol)
        if coin_and_price:
            await ctx.send(f"The Current Price of {symbol} is {coin_and_price[0]}")
        else:
            await ctx.send(
                "I'm having trouble finding that cryptocurrency, check for typos and try again :)"
            )

    @commands.command(name="newacc", help="Create new Papertrading acc")
    async def newacc(self, ctx) -> None:
        """
        creates new paper trading account

        """
        print("\n\n\n" + str(str(ctx.author)) + "\n\n\n")
        x = str(ctx.author)
        result = newaccount(x)
        await ctx.send(result)

    @commands.command(name="buy", help="Buy Crypto Currency")
    async def buy(self, ctx, symbol: str, amount: int) -> None:
        """
        trades X amount for dollars for Y amount of another currency

        :param symbol: currency symbol to buy
        :type symbol: str
        :param amount: amount to buy for
        :type amount: int
        """
        x = str(ctx.author)
        if exist(x):
            user = load(x)
            result = user.buy(symbol.upper(), float(amount))
            save(user, x)
            await ctx.send(result)
        else:
            await ctx.send("No account to buy with! enter: nb.newacc to create one")

    @commands.command(name="sell", help="Sell Crypto Currency")
    async def sell(self, ctx, symbol: str, amount: int) -> None:
        """
        trades  X amount of currency for Y amount of  dollars

        :param symbol: currency to sell
        :type symbol: str
        :param amount: amount to sell
        :type amount: int
        """
        x = str(ctx.author)
        if exist(x):
            user = load(x)
            result = user.sell(symbol.upper(), float(amount))
            save(user, x)
            await ctx.send(result)
        else:
            await ctx.send("No account to sell with.... Enter: nb.newacc to create one")

    @commands.command(name="balance", help="Get cash balance of paper trading account")
    async def balance(self, ctx) -> None:
        """
        shows user's balance

        """
        x = str(ctx.author)
        if exist(x):
            user = load(x)
            result = user.balance
            await ctx.send(result)
        else:
            await ctx.send("No account... enter: nb.newacc to create one")

    @commands.command(name="coins", help="Get list of coins you have")
    async def coins(self, ctx) -> None:
        """
        shows a list of coins owned by user

        """
        x = str(ctx.author)
        if exist(x):
            user = load(x)
            if user.coins:
                result = str(user.coins)
                await ctx.send(result[1:-1])
            else:
                await ctx.send("You haven't purchased any coins yet!")
        else:
            await ctx.send("No account... enter: nb.newacc to create one")

    @commands.command(name="portfolio", help="Get value of portfolio")
    async def portfolio(self, ctx) -> None:
        """
        shows user's portfolio

        """
        x = str(ctx.author)
        if exist(x):
            user = load(x)
            user.updatePortfolioPrice()
            result = user.portfolioValue
            await ctx.send(result)
        else:
            await ctx.send("No account... enter: nb.newacc to create one")


def setup(bot):
    bot.add_cog(Crypto(bot))
