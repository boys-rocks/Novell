import discord
from discord.ext import commands
from helpers import logHelper
from bot import collection
import time


def time_format(seconds: int):
    if seconds is not None:
        seconds = int(seconds)
        d = seconds // (3600 * 24)
        h = seconds // 3600 % 24
        m = seconds % 3600 // 60
        s = seconds % 3600 % 60
        if d > 0:
            return f"{d:02d}D {h:02d}H {m:02d}m {s:02d}s"
        elif h > 0:
            return f"{h:02d}H {m:02d}m {s:02d}s"
        elif m > 0:
            return f"{m:02d}m {s:02d}s"
        elif s > 0:
            return f"{s:02d}s"
    return None


class Base(commands.Cog):
    START_TIME = time.time_ns()

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

        """
        await ctx.send("Cogs working.")

    @commands.command(help="Checks Latency/ping")
    async def ping(self, ctx):
        """
        checks ping/latency

        """

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

        :param extension: cogs/command to reload
        :type extension: str
        """
        self.bot.unload_extension(f"cogs.{extension}")
        self.bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"The module '{extension}' has been reloaded successfully!")

    @commands.command(name="uptime")
    async def get_uptime(self, ctx):
        """
        get uptime for bot

        """
        # convert nanoseconds into seconds
        uptime_in_seconds = (time.time_ns() - self.START_TIME) * 10 ** -9

        uptime = time_format(uptime_in_seconds)
        if not uptime is None:
            try:
                await ctx.send(f"been running from last {uptime}. I'm tired ")
            except Exception as error:
                print(error)
        else:
            await ctx.send("failed to get uptime...")


def setup(bot):
    bot.add_cog(Base(bot))
