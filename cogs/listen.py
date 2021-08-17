from discord.ext import commands
class Listen(commands.Cog):
    """
    Bot Voice Channel Commands
    """
    def __init__(self, bot):
        self.bot = bot
    @commands.command(help = 'Bot joins voice channel')
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
    @commands.command(help = 'Bot leaves voice channel')
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()
def setup(bot):
    bot.add_cog(Listen(bot))