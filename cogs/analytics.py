import discord
from discord.ext import commands
from bot import collection

class Analytics(commands.Cog):
    """
    Analytics Module
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Gets frequency of command")
    async def freq(self, ctx, command):
        freq = collection.find_one({"_id":"word_command_freq"})
        clean_freq_data = command
        if "." in clean_freq_data:
            clean_freq_data = clean_freq_data.replace(".","(Dot)")
        if "$" in clean_freq_data:
            clean_freq_data = clean_freq_data.replace("$","(Dollar_Sign)")
        await ctx.send(command + " has been used "+str(freq[clean_freq_data]) + " times!")


def setup(bot):
    bot.add_cog(Analytics(bot))
