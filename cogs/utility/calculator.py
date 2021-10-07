import ast
import discord
from discord.ext import commands


class Calculator(commands.Cog):
    "Calculator Module"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Simple Calculator command")
    async def clc(self, ctx, *, query: str) -> None:
        """
        simple calculator using eval function

        :param ctx: discord context manager
        :type ctx: discord.ContextManager
        :param query: equation to solve
        :type query: str
        """
        problem = "".join(query)
        try:
            result = ast.literal_eval(problem)
        except ZeroDivisionError:
            await ctx.reply("number cannot be divided by 0.")
            return
        except SyntaxError:
            await ctx.reply("Only numbers are supported.")
            return
        except:
            await ctx.reply("Invalid Equation, Please recheck and try again.")
            return
        await ctx.reply(f"```{problem} = {result}```")

    @commands.command(help="converts decimal number to binary number")
    async def convert_to_bin(self, ctx, dec: int) -> None:
        """
        convert decimal number to binary number

        :param dec: decimal number
        :type dec: int
        """
        if isinstance(dec, int):
            result = bin(dec).replace("0b", "")
            await ctx.send(result)
        else:
            await ctx.send("I can only convert integers")

    @commands.command(help="convets binary number to decimal number")
    async def convert_from_bin(self, ctx, bin: str) -> None:
        """
        converts binary number to decimal number

        :param bin: binary number
        :type bin: str
        """
        try:
            result = int(bin, 2)
        except ValueError:
            result = "This is not a binary number"
        await ctx.send(result)

    @commands.command(help="Converts decimal to hexadecimal")
    async def convert_to_hex(self, ctx, dec: int) -> None:
        """
        converts decimal number to hexadecimal number

        :param dec: decimal number
        :type dec: int
        """
        if isinstance(dec, int):
            result = hex(dec).removeprefix("0x").upper()
            await ctx.send(result)
        else:
            await ctx.send("I can only convert integers")

    @commands.command(help="Converts hexadecimal to decimal")
    async def convert_from_hex(self, ctx, hex: str) -> None:
        """
        converts hexadecimal number to decimal number

        :param hex: hexadecimal number
        :type hex: str
        """
        try:
            result = int(hex, 16)
        except ValueError:
            result = "This is not a hexadecimal number"
        await ctx.send(result)


def setup(bot):
    bot.add_cog(Calculator(bot))
