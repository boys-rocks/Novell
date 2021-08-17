import discord
from discord.ext import commands
import requests


class Trivia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def trivia(self, ctx):
        with requests.get(url=f"http://jservice.io/api/random") as response:
            answer = response.json()[0]['answer']
            await ctx.send(response.json()[0]['question'])
            guess = await self.bot.wait_for(
                'message', check=lambda message: message.author == ctx.author)
            if guess.content.lower() == answer.lower():
                await ctx.send(
                    f'You are correct ✓✓. {guess.content.lower()} is the right answer'
                )
            else:
                await ctx.send(
                    f'Incorrect ✗✗. Correct answer is {answer.lower()} ')


def setup(bot):
    bot.add_cog(Trivia(bot))
