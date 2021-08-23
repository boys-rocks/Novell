import discord
from discord.ext import commands


class Calculator(commands.Cog):
    "Calculator Module"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Calculator command")
    async def clc(self, ctx, *query):
        problem = " ".join(query)
        result = eval(problem)
        await ctx.send(f"```{problem} = {result}```")

    @commands.command()
    async def convert_to_bin(self, ctx, dec: int):
        """
        Converts decimal to binary
        """
        if isinstance(dec, int):
            result = bin(dec).replace("0b", "")
            await ctx.send(result)
        else:
            await ctx.send("I can only convert integers")

    @commands.command()
    async def convert_from_bin(self, ctx, bin: str):
        """
        Converts binary to decimal
        """
        try:
            result = int(bin, 2)
        except ValueError:
            result = "This is not a binary number"
        await ctx.send(result)

    @commands.command()
    async def convert_to_hex(self, ctx, dec: int):
        """
        Converts decimal to hexadecimal
        """
        if isinstance(dec, int):
            result = hex(dec).removeprefix("0x").upper()
            await ctx.send(result)
        else:
            await ctx.send("I can only convert integers")

    @commands.command()
    async def convert_from_hex(self, ctx, hex: str):
        """
        Converts hexadecimal to decimal
        """
        try:
            result = int(hex, 16)
        except ValueError:
            result = "This is not a hexadecimal number"
        await ctx.send(result)


def setup(bot):
    bot.add_cog(Calculator(bot))
