import discord
from discord.ext import commands
from random import choice


class RockPaperScissors(commands.Cog):
    """
    Play Rock Paper Scissors
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="rps",
        help="Play Rock Paper Scissors",
        aliases=["play_rps", "rock_paper_scissors"],
    )
    async def rock_paper_scissors(self, ctx):
        """
        starts rock paper scissors game with computer

        """
        avl_moves = ["rock", "paper", "scissors"]
        await ctx.send(f"rock, paper, or scissors? Choose wisely...")

        def check(msg):
            return (
                msg.author == ctx.author
                and msg.channel == ctx.channel
                and msg.content.lower() in avl_moves
            )

        usr_move = (await self.bot.wait_for("message", check=check)).content
        comp_move = choice(avl_moves)
        if usr_move == "rock":
            if comp_move == "rock":
                await ctx.send(
                    f"Well, that was weird. We tied.\nYour choice: {usr_move}\nMy choice: {comp_move}"
                )
            elif comp_move == "paper":
                await ctx.send(
                    f"Nice try, but I won that time!!\nYour choice: {usr_move}\nMy choice: {comp_move}"
                )
            elif comp_move == "scissors":
                await ctx.send(
                    f"Aw, you beat me. It won't happen again!\nYour choice: {usr_move}\nMy choice: {comp_move}"
                )

        elif usr_move == "paper":
            if comp_move == "rock":
                await ctx.send(
                    f"The pen beats the sword? More like the paper beats the rock!!\nYour choice: {usr_move}\nMy choice: {comp_move}"
                )
            elif comp_move == "paper":
                await ctx.send(
                    f"Oh, wacky. We just tied. I call a rematch!!\nYour choice: {usr_move}\nMy choice: {comp_move}"
                )
            elif comp_move == "scissors":
                await ctx.send(
                    f"Aw man, you actually managed to beat me.\nYour choice: {usr_move}\nMy choice: {comp_move}"
                )

        elif usr_move == "scissors":
            if comp_move == "rock":
                await ctx.send(
                    f"HAHA!! I JUST CRUSHED YOU!! I rock!!\nYour choice: {usr_move}\nMy choice: {comp_move}"
                )
            elif comp_move == "paper":
                await ctx.send(
                    f"Bruh. >: |\nYour choice: {usr_move}\nMy choice: {comp_move}"
                )
            elif comp_move == "scissors":
                await ctx.send(
                    f"Oh well, we tied.\nYour choice: {usr_move}\nMy choice: {comp_move}"
                )
        else:
            await ctx.send("invalid move/choice")


def setup(bot):
    bot.add_cog(RockPaperScissors(bot))
