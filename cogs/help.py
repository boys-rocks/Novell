import sys
import discord
from discord.ext import commands 
from helpers import getPrice, checkParams

class help(commands.Cog):
    """
    Main help Module for now
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help='Help command helps help with commands')
    async def help(self, ctx, args=None):
        help_embed = discord.Embed(title="NUUB_BOT Help!")
        command_names_list = [x.name for x in self.bot.commands]

        # If there are no arguments, just list the commands:
        if not args:
            help_embed.add_field(
                name="List of supported commands:",
                value="\n".join([str(i+1)+". "+x.name for i,x in enumerate(self.bot.commands)]),
                inline=False
            )
            help_embed.add_field(
                name="Details",
                value="Type `*help <command name>` for more details about each command.",
                inline=False
            )

        # If the argument is a command, get the help text from that command:
        elif args in command_names_list:
            help_embed.add_field(
                name=args,
                value=self.bot.get_command(args).help,
                inline=False
            )
            help_embed.add_field(
                name="Parameters",
                value=checkParams.checkCommandParams(self.bot, args),  
                inline=False
            )
        # If someone is just trolling:
        else:
            help_embed.add_field(
                name="Nope.",
                value="Don't think I got that command, boss!"
            )

        await ctx.send(embed=help_embed)

def setup(bot):
    bot.add_cog(help(bot))
    