import discord
from discord.ext import commands
from bot import collection


def clean_chars(command: str) -> str:
    """
    replaces character with mongodb characters format

    :param command: discord command to be converted
    :type command: str
    :return: converted command
    :return type: str
    """
    clean_freq_data = command
    if "." in clean_freq_data:
        clean_freq_data = clean_freq_data.replace(".", "(Dot)")
    if "$" in clean_freq_data:
        clean_freq_data = clean_freq_data.replace("$", "(Dollar_Sign)")
    return clean_freq_data


def clean_chars_reverse(command: str) -> str:
    """
    replaces mongodb characters format with standard characters

    :param command: discord command to be converted
    :type command: str
    :return: converted command
    :return type: str
    """
    clean_freq_data = command
    if "(Dot)" in clean_freq_data:
        clean_freq_data = clean_freq_data.replace("(Dot)", ".")
    if "(Dollar_Sign)" in clean_freq_data:
        clean_freq_data = clean_freq_data.replace("(Dollar_Sign)", "$")
    return clean_freq_data


def get_top(number: int) -> list[str]:
    """
    shows most used commands in a server

    :param number:
    :type number: int
    :return: list of top commands
    :return type: list[str]
    """
    words = collection.find({"_id": "word_command_freq"})
    pairlist = []
    for word in words:
        for each in word:
            cleaned_key = clean_chars_reverse(each)
            if cleaned_key[0:3] == "nb.":
                pairlist.append((cleaned_key, word[each]))
    pairlist.sort(key=lambda pair: pair[1], reverse=True)
    return pairlist[:number]


class Analytics(commands.Cog):
    """
    Analytics Module
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Gets frequency of command")
    async def freq(self, ctx, command: str) -> None:
        freq = collection.find_one({"_id": "word_command_freq"})
        clean_freq_data = clean_chars(command)
        try:
            await ctx.send(
                command + " has been used " + str(freq[clean_freq_data]) + " times!"
            )
        except Exception as e:
            await ctx.send("Command not found")

    @commands.command(help="Gets frequency of most used commands")
    async def topcommands(self, ctx, number: int = 10) -> None:
        commands = get_top(int(number))
        all_commands = ""
        for command in commands:
            formatted_command = str(command[0]) + ": " + str(command[1])
            all_commands = all_commands + formatted_command + "\n"
        await ctx.send(all_commands)


def setup(bot):
    bot.add_cog(Analytics(bot))


print()
