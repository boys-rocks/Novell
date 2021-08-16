import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.send(embed=discord.Embed(title=f'You have been kicked from {ctx.guild}', description=f'Reason: {reason}'))
        await member.kick(reason=reason)
        await ctx.send(embed=discord.Embed(title='Kicked: ', description=f'{member} for {reason}.'))

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        await member.send(embed=discord.Embed(title=f'You have been banned from {ctx.guild}', description=f'Reason: {reason}'))
        await member.ban(reason=reason)
        await ctx.send(embed=discord.Embed(title='Banned: ', description=f'{member} for {reason}.'))

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send(embed=discord.Embed(title='Purged: ', description=f'{limit} messages.'), delete_after=5)


def setup(bot):
    bot.add_cog(Moderation(bot))
