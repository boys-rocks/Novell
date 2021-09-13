import discord
from discord.ext import commands
from helpers import logHelper
from bot import collection


class Base(commands.Cog):
    """
    Initail event Module and bot settings
    merged test cog into here
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print("Ready..")
        print("Logged in as: ", self.bot.user)
        print("Prefix: ", self.bot.command_prefix)
        print("Latency: ", round(self.bot.latency * 1000), "ms")
        logHelper.logger.info(f"Logged in as: {self.bot.user}")
        logHelper.logger.info("Latency: {}ms".format(round(self.bot.latency * 1000)))

    @commands.command(help="Changes prefix ")
    async def prefix(self, ctx, prefix: str) -> None:
        """
        Changes bot's prefix

        :param ctx: discord ContextManager
        :type ctx: discord.ContextManager
        :param prefix: new prefix
        :type prefix: str
        """
        collection.update_one({"_id": ctx.guild.id}, {"$set": {"prefix": prefix}})
        await ctx.send(
            embed=discord.Embed(
                title="Updated Prefix: ", description=f"New prefix: {prefix}"
            )
        )

        def __init__(self, bot):
            self.bot = bot

    @commands.command(help="Checks if Cogs are working")
    async def cogstest(self, ctx) -> None:
        """
        checks if cogs/commands are working

        :param ctx: discord context manager
        :type ctx: discord.ContextManager
        """
        await ctx.send("Cogs working.")

    @commands.command(help="Checks Latency/ping")
    async def ping(self, ctx):
        """
        checks ping/latency

        :param ctx: discord context manager
        :type ctx: discord.ContextManager
        """
        import time

        time_1 = time.perf_counter()
        await ctx.trigger_typing()
        time_2 = time.perf_counter()
        latency = round((time_2 - time_1) * 1000)

        em = discord.Embed(title="Pong!", description=f"{latency}ms")
        await ctx.send(embed=em)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension: str) -> None:
        """
        loads cogs/commands

        :param ctx: discord context manager
        :type ctx: discod.ContextManager
        :param extension: cogs/command to load
        :type extension: str
        """
        self.bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"The module {extension} has been loaded successfully!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension: str) -> None:
        """
        unloads cogs/commands

        :param ctx: discord context manager
        :type ctx: discod.ContextManager
        :param extension: cogs/command to unload
        :type extension: str
        """
        self.bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"The module '{extension}' has been unloaded successfully!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension: str) -> None:
        """
        reloads cogs/commands i.e unload and then load it again

        :param ctx: discord context manager
        :type ctx: discod.ContextManager
        :param extension: cogs/command to reload
        :type extension: str
        """
        self.bot.unload_extension(f"cogs.{extension}")
        self.bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"The module '{extension}' has been reloaded successfully!")


def setup(bot):
    bot.add_cog(Base(bot))
