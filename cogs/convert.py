from discord.ext import commands


class Convert(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def convert_to_bin(self, ctx, dec: int):
        if isinstance(dec, int):
            result = bin(dec).replace("0b", "")
            await ctx.send(result)
        else:
            await ctx.send("I can only convert integers")

    @commands.command()
    async def convert_from_bin(self, ctx, bin: str):
        try:
            result = int(bin, 2)
        except ValueError:
            result = "This is not a binary number"
        await ctx.send(result)

    @commands.command()
    async def convert_to_hex(self, ctx, dec: int):
        if isinstance(dec, int):
            result = hex(dec).removeprefix("0x").upper()
            await ctx.send(result)
        else:
            await ctx.send("I can only convert integers")

    @commands.command()
    async def convert_from_hex(self, ctx, hex: str):
        try:
            result = int(hex, 16)
        except ValueError:
            result = "This is not a hexadecimal number"
        await ctx.send(result)


def setup(bot):
    bot.add_cog(Convert(bot))
