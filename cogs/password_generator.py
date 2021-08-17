# Standard Libraries
import random

# Third party libraries
import discord
from discord.ext import commands


class PasswordGenerator(commands.Cog):

    """
    Generates a password from unicode decimal ranges.
    """

    def __init__(self, client):
        """
        Initialize cog.
        """
        self.client = client

    @commands.command(help = "Password from unicode decimal ranges.")
    async def make_password(self, ctx):

        """
        Generates a password containing upper and lowercase alphabetic characters, numeric characters, and special
        characters. Will not push to user until one of each provided.

        :param ctx: Context for asynchronous / discord library functionality.
        :return: Password private messaged to member who executed command.
        """

        # Generate list of special characters.
        special_characters = []
        for unicode_value in range(33, 127):
            if unicode_value in range(33, 48) or unicode_value in range(58, 65) \
            or unicode_value in range(91, 97) or unicode_value in range(123, 127):
                special_characters.append(chr(unicode_value))

        while True:
            # Initialize on each loop.
            password = ''
            has_lower_alpha, has_upper_alpha, has_numeric = False, False, False

            # Randomly select 20 characters in unicode decimal range 33 to 126
            for char in range(20):
                unicode_num = random.randint(33, 126)
                password += chr(unicode_num)

            # Perform Check for each type.
            for char in password:
                if char.isupper():
                    has_upper_alpha = True
                elif char.islower():
                    has_lower_alpha = True
                elif char.isdigit():
                    has_numeric = True
            has_special_char = any(each in special_characters for each in password)

            # Rerun loop if any type is missing or end loop otherwise.
            if has_upper_alpha == False or has_lower_alpha == False \
                    or has_numeric == False or has_special_char == False:
                continue
            else:
                break

        # Private message user the password generated
        await ctx.author.send(f"Disclaimer: We are not responsible for compromised accounts. "f"\nPassword: {password}")


# Standard cog setup.
def setup(client):
    client.add_cog(PasswordGenerator(client))
