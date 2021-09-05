import discord
from discord.ext import commands
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import random
import aiohttp
import string


class genav(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Generate random av")
    async def genav(self, ctx, seed=None):
        if seed is None:
            seed = "".join(random.sample(string.ascii_letters, random.randint(1, 10)))
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://avatars.dicebear.com/api/avataaars/{seed}.svg?mood[]=happy"
            ) as resp:
                img_data = await resp.content.read()
        with open("./temp/avatar.svg", "wb") as handler:
            handler.write(img_data)
        drawing = svg2rlg("./temp/avatar.svg")
        renderPM.drawToFile(drawing, "./temp/avatar_mod.png", fmt="PNG")
        with open("./temp/avatar_mod.png", "rb") as fhand:
            file = discord.File(fhand, filename="avatar.png")
        await ctx.reply(file=file)

    @commands.command(help="Generate random micah")
    async def genmh(self, ctx, seed=None):
        if seed is None:
            seed = "".join(random.sample(string.ascii_letters, random.randint(1, 10)))
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://avatars.dicebear.com/api/micah/{seed}.svg?mood[]=happy"
            ) as resp:
                img_data = await resp.content.read()
        with open("./temp/micah.svg", "wb") as handler:
            handler.write(img_data)
        drawing = svg2rlg("./temp/micah.svg")
        renderPM.drawToFile(drawing, "./temp/micah_mod.png", fmt="PNG")
        with open("./temp/micah_mod.png", "rb") as fhand:
            file = discord.File(fhand, filename="micah.png")
        await ctx.reply(file=file)


def setup(bot):
    bot.add_cog(genav(bot))
