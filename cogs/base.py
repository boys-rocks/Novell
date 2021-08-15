from discord.ext import commands
from helpers import logHelper
class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready..')
        print('Logged in as: ', self.bot.user)
        print('Prefix: ', self.bot.command_prefix)
        print('Latency: ', round(self.bot.latency*1000), 'ms')
        logHelper.logger.info(f'Logged in as: {self.bot.user}' )
        logHelper.logger.info('Latency: {}ms'.format(round(self.bot.latency*1000)))      
def setup(bot):
    bot.add_cog(Base(bot))