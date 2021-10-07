import discord
from discord.ext import commands
from random import choice
from resources.higherlowerdata import data
from resources.higherlowerdata import reaction_negative, reaction_positive


class HigherLower(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Play Higher/Lower (instagram follower edition).")
    async def higherlower(self, ctx) -> None:
        """
        Play Higher/Lower (instagram follower edition).

        """

        def pick():
            """
            picks up a random entry for the game

            :return: a random entry from the higherlower data
            :rtype: dict()
            """
            return choice(data)

        def format_ques(question: dict) -> str:
            """
            returns formatted question

            :param question: question/entry
            :type question: dict
            :return: formatted question
            :rtype: str
            """
            return f"{question['name']}, a {question['description']}, from {question['country']} "

        await ctx.send(
            f"""
              ｈｉｇｈｅｒ ／ ｌｏｗｅｒ
              """
        )
        is_playing = True
        score = 0
        while is_playing:
            while True:
                question_one = pick()
                question_two = pick()
                if question_one == question_two:
                    continue
                await ctx.send(
                    f"```Compare A: {format_ques(question_one)}\n\t\t\t VS \nCompare B: {format_ques(question_two)}\n\nWho has more followers? Type 'A' or 'B':```"
                )
                guess = await self.bot.wait_for(
                    "message",
                    check=lambda message: message.author == ctx.author,
                )

                if guess.content.lower() == "a":
                    guess = question_one["follower_count"]
                elif guess.content.lower() == "b":
                    guess = question_two["follower_count"]
                if guess == max(
                    question_one["follower_count"], question_two["follower_count"]
                ):
                    score += 1
                    await ctx.send(
                        f"```{choice(reaction_positive)}, Your score is {score} ```"
                    )

                else:
                    await ctx.send(
                        f"```{choice(reaction_negative)}. Final score: {score}```"
                    )
                    break
            is_playing = False


def setup(bot):
    bot.add_cog(HigherLower(bot))
