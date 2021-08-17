import discord
from discord.ext import commands
from resources.hangman_data import word_list
from random import choice

LOGO = "**ｈａｎｇｍａｎ**\n\n``rule:\n1.you will get 5 lives\n2.with each incorrect guess, you lose one live\n3.if you can guess all the alphabets in the word with live remaining you WIN\n4.Otherwise, you LOSE.``"


async def make_blanks(rng):
    blanks = list()
    for _ in range(rng):
        blanks.append("_̲_̲_̲")
    return blanks


class Hangman(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hangman(self, ctx):
        chosen_word = choice(word_list)
        word_length = len(chosen_word)

        self.end_of_game = False
        self.lives = 5
        await ctx.send(f"{LOGO}")
        blanks = await make_blanks(len(chosen_word))
        await ctx.send(f'```{"   ".join(blanks)}```')
        while not self.end_of_game:
            guess = await self.bot.wait_for(
                'message', check=lambda message: message.author == ctx.author)
            if guess.content.lower() == "exit":
                self.end_of_game = True
                break
            # Check guessed letter
            if guess.content.lower() in blanks:
                await ctx.send(
                    f"```You've already guessed {guess.content.lower()}.```")
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess.content.lower():
                    blanks[position] = letter

            # Check if user is wrong.
            if guess.content.lower() not in chosen_word:
                await ctx.send(
                    f"```You've guessed {guess.content.lower()}, that's not in the word. You lose a life ```"
                )
                self.lives -= 1
                if self.lives == 0:
                    self.end_of_game = True
                    await ctx.send("You LOSE !.")
                    break

            # Join all the elements in the list and turn it into a String.
            await ctx.send(f"```{'  '.join(blanks)}```")

            # Check if user has got all letters.
            if "_̲_̲" not in blanks:
                self.end_of_game = True
                await ctx.send("You WIN !!!.")
                break
            await ctx.send(f"```lives remaining: {self.lives}```")


def setup(bot):
    bot.add_cog(Hangman(bot))
