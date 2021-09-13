import discord
from discord.ext import commands


class Moderation(commands.Cog):
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
            "tensei-shinra",
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


def setup(bot):
    bot.add_cog(Moderation(bot))
