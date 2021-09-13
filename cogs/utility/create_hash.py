# Standard library modules.
import hashlib

# Third party modules.
import discord
from discord.ext import commands


class Hash(commands.Cog):
    """
    Cog provides a command for the user to see their string hashed.
    """

    def __init__(self, client):
        """Initialize cog"""
        self.client = client

    @commands.command(
        name="hash",
        help="Command reads in user specified algorithm and string to output hash.",
    )
    async def make_hash(self, ctx, algorithm, *, user_value: str):
        """
        Command reads in user specified algorithm and string to output hash.

        :param ctx: Discord context of command.
        :param algorithm: User specifies hashing algorithm. Value must be md5, sha1, sha256, or sha512.
        :param user_value: User input string. Can be any length greater than 1.
        :return: No return. Print hash to dialogue window.
        """

        # Checks user algorithm argument input.
        if algorithm.lower() == "md5":
            a_hash = hashlib.md5()
        elif algorithm.lower() == "sha1":
            a_hash = hashlib.sha1()
        elif algorithm.lower() == "sha256":
            a_hash = hashlib.sha256()
        elif algorithm.lower() == "sha512":
            a_hash = hashlib.sha512()
        else:
            await ctx.send("Invalid input. Please provide all required arguments.")
            await ctx.send("Form: .make_hash <hashing algorithm> <string>")
            await ctx.send("Available hashing algorithms: md5, sha1, sha256, sha512")

        # Encodes and outputs hash
        a_hash.update(user_value.encode("utf-8"))
        await ctx.send(a_hash.hexdigest())

    @make_hash.error
    async def on_hash_command_error(self, ctx, error):
        """Catches exception when user does not provide all arguments. Outputs required format"""

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Invalid input. Please provide all required arguments.")
            await ctx.send("Form: .make_hash <hashing algorithm> <string>")
            await ctx.send("Available hashing algorithms: md5, sha1, sha256, sha512")


# Standard cog setup
def setup(client):
    client.add_cog(Hash(client))
