import discord
from discord.ext import commands
from helpers import logHelper
<<<<<<< HEAD
from bot import collection
=======
>>>>>>> nuub-botV0.02


class Base(commands.Cog):
    """
    Initail event Module and bot settings
    merged test cog into here
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready..")
        print("Logged in as: ", self.bot.user)
        print("Prefix: ", self.bot.command_prefix)
        print("Latency: ", round(self.bot.latency * 1000), "ms")
        logHelper.logger.info(f"Logged in as: {self.bot.user}")
        logHelper.logger.info("Latency: {}ms".format(round(self.bot.latency * 1000)))

    @commands.command(help="Chage prefix command")
    async def prefix(self, ctx, prefix):
        collection.update_one({"_id": ctx.guild.id}, {"$set": {"prefix": prefix}})
        await ctx.send(
            embed=discord.Embed(
                title="Updated Prefix: ", description=f"New prefix: {prefix}"
            )
        )

        def __init__(self, bot):
            self.bot = bot

    @commands.command(help="Checks if Cogs are working")
    async def cogstest(self, ctx):
        await ctx.send("Cogs working.")

    @commands.command(help="Check Latency")
    async def ping(self, ctx):
        em = discord.Embed(
            title="Pong!", description=str(round(self.bot.latency * 1000)) + "ms"
        )
        await ctx.send(embed=em)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension):
        self.bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"The module {extension} has been loaded successfully!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"The module '{extension}' has been unloaded successfully!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension):
        self.bot.unload_extension(f"cogs.{extension}")
        self.bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"The module '{extension}' has been reloaded successfully!")


def setup(bot):
    bot.add_cog(Base(bot))
