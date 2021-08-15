import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(embed=discord.Embed(title='Kicked: ', description=f'{member} for {reason}.'))

def setup(bot):
    bot.add_cog(Moderation(bot))

