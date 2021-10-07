import ast
import discord
from discord.ext import commands


class Moderation(commands.Cog):
    slow_mode_status = False
    """
    Moderation Module
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Kicks Specified User")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None) -> None:
        """
        kicks specified user from a server

        :param ctx: context manager
        :type ctx: discord.ContextManager
        :param member: discord member
        :type member: discord.Member
        :param reason: reason for kick out , defaults to None
        :type reason: str, optional
        """
        await member.send(
            embed=discord.Embed(
                title=f"You have been kicked from {ctx.guild}",
                description=f"Reason: {reason}",
            )
        )
        await member.kick(reason=reason)
        await ctx.send(
            embed=discord.Embed(title="Kicked: ", description=f"{member} for {reason}.")
        )

    @commands.command(help="Bans Specified User")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None) -> None:
        """
        bans a specified user from a server

        :param ctx: context manager for discord
        :type ctx: discord.ContextManager
        :param member: discord member class
        :type member: discord.Member
        :param reason: reason for the ban, defaults to None
        :type reason: str, optional
        """
        await member.send(
            embed=discord.Embed(
                title=f"You have been banned from {ctx.guild}",
                description=f"Reason: {reason}",
            )
        )
        await member.ban(reason=reason)
        await ctx.send(
            embed=discord.Embed(title="Banned: ", description=f"{member} for {reason}.")
        )

    @commands.command(
        help="Purges Messages",
        aliases=[
            "allmightypush",
        ],
    )
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit=1000) -> None:
        """
        deletes specified number messages from a channel

        :param ctx: context manager for discord
        :type ctx: discord.ContextManager
        :param limit: number of messages to delete, defaults to 1000
        :type limit: int, optional
        """
        await ctx.channel.purge(limit=limit)
        await ctx.send(
            embed=discord.Embed(title="Purged: ", description=f"{limit} messages."),
            delete_after=5,
        )

    @commands.command(name="slowmode", help="sets delay for messages")
    @commands.has_permissions(manage_messages=True)
    async def slow_mode(self, ctx, delay: str = None):
        """
        set delay in a channel


        :param delay: delay time, defaults to None
        :type delay: str, optional
        """
        if delay is None and self.slow_mode_status is False:
            self.slow_mode_status = True
            await ctx.send("Slow Mode Activated with `1 minute` delay.")
            await ctx.channel.edit(slowmode_delay=60)
        elif delay is None and self.slow_mode_status is True:
            self.slow_mode_status = False
            await ctx.send("Slow Mode Deactivated.")
            await ctx.channel.edit(slowmode_delay=0)
        else:
            try:
                self.slow_mode_status = True
                delay_mod = delay.lower()
                if (
                    len(delay[: delay_mod.find("h")]) > 1
                    or len(delay[delay_mod.find("h") : delay_mod.find("m")]) > 2
                    or len(delay_mod[delay_mod.find("m") : -1]) > 2
                ):
                    await ctx.send("Invalid delay time `expected format:0h00m00s`")
                    return
                if "s" in delay_mod or "h" in delay_mod or "m" in delay_mod:
                    delay_mod = delay_mod.replace("s", "")
                    delay_mod = delay_mod.replace("m", "*60+")
                    delay_mod = delay_mod.replace("h", "*3600+")
                    if delay_mod.endswith("+"):
                        delay_mod = delay_mod[:-1]
                    total_delay = ast.literal_eval(delay_mod)
                    if total_delay > 21600:
                        await ctx.send("Invalid Delay (max limit is 6hrs)")
                        return
                    else:
                        await ctx.send(f"Slow Mode activated with `{delay}` delay.")
                        await ctx.channel.edit(slowmode_delay=total_delay)
                else:
                    await ctx.send(f"Slow Mode activated with `{delay} seconds` delay.")
                    await ctx.channel.edit(slowmode_delay=int(delay))

            except Exception as error:
                await ctx.send(f"Invalid Delay{error}")
                print(error)


def setup(bot):
    bot.add_cog(Moderation(bot))
