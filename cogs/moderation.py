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
    async def kick(self, ctx, member: discord.Member, *, reason=None):
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
    async def ban(self, ctx, member: discord.Member, *, reason=None):
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

    @commands.command(help="Purges Messages")
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send(
            embed=discord.Embed(title="Purged: ", description=f"{limit} messages."),
            delete_after=5,
        )

    @commands.command(help="Unbans user with ID")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: int):
        user = await self.bot.fetch_user(member)
        await ctx.guild.unban(user)
        embed = discord.Embed(
            title="Unbanned",
            description=f"{member} was unbanned successfully..",
        )
        await ctx.send(embed=embed)

    @commands.command(help="Deafens member")
    @commands.has_guild_permissions(deafen_members=True)
    async def deafen(self, ctx, usr: discord.Member):
        await usr.edit(deafen=True)
        embed = discord.Embed(
            title="Deafened",
            description=f"{usr} was deafened successfully..",
        )
        await ctx.send(embed=embed)

    @commands.command(help="Undeafens member")
    @commands.has_guild_permissions(deafen_members=True)
    async def undeafen(self, ctx, usr: discord.Member):
        await usr.edit(deafen=False)
        embed = discord.Embed(
            title="Undeafened",
            description=f"{usr} was undeafened successfully..",
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Moderation(bot))
