import re

from discord.ext import commands
from helpers.tic_tac_toe.tic_tac_toe_game import TicTacToeGame
from helpers import ask_for_acceptance


class TicTacToe(commands.Cog):
    """
    Play Tic-Tac-Toe against another discord user or against the computer with three difficulties:
     - easy
     - difficult
     - impossible
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play_tic_tac_toe(self, ctx, difficulty: str):
        """
        Available difficulties:
         - easy
         - difficult
         - impossible
        """

        if difficulty.lower() not in ["easy", "difficult", "impossible"]:
            await ctx.send("Unavailable difficulty")
            return
        game = TicTacToeGame("X", "O", TicTacToeGame.PLAYER, difficulty)
        while not game.check_game_over():
            await ctx.send(game.to_string(True))
            await ctx.send("Where do you want to go?")
            move = await self.bot.wait_for(
                "message", check=lambda message: message.author == ctx.author)
            if move.content.strip().lower() == "exit":
                await ctx.send("Exiting...")
                return
            try:
                move = int(move.content.strip().lower())
            except ValueError:
                await ctx.send("This doesn't look like a number")
                continue
            if move not in game.possible_moves():
                await ctx.send("You can't choose field " + str(move))
                continue
            game.make_move(move)
            if game.check_game_over():
                break
            await ctx.send(game.to_string())
            ai_move = game.get_ai_move()
            await ctx.send("I choose " + str(ai_move))
            game.make_move(ai_move)
        winner = game.get_winner()
        await ctx.send(game.to_string())
        if winner == game.PLAYER:
            await ctx.send("You won! Congratulation!")
        elif winner == game.COMPUTER:
            await ctx.send("I won! Better luck next time!")
        else:
            await ctx.send("It's a Draw! Wanna play again?")

    @commands.command()
    async def play_tic_tac_toe_multiplayer(self, ctx, opponent):
        """
        Play Tic-Tac-Toe against someone on your discord server!
        Simply write play_tic_tac_toe_multiplayer and mention them
        """
        challenger = ctx.author
        opponent = ctx.guild.get_member(int(re.sub("[^0-9]", "", opponent)))
        invite = opponent.mention + "! " + challenger.mention + " is in inviting you to a game of Tic-Tac-Toe. Accept?"
        if ask_for_acceptance.ask(invite, opponent, ctx.channel, self.bot):
            await ctx.send("An epic Tic-Tac-Toe Duel is about to start between " +
                           challenger.mention + " and " + opponent.mention)
        else:
            await ctx.send("Hey " + challenger.mention + "! I am sad to inform you " +
                           opponent.mention + " hasn't accepted the invite")
            return
        active_player = opponent
        game = TicTacToeGame("X", "O", TicTacToeGame.PLAYER, "")
        while not game.check_game_over():
            await ctx.send("It is " + active_player.mention + "'s turn!")
            await ctx.send(game.to_string(including_number_grid=True))
            move = await self.bot.wait_for(
                "message", check=lambda message: message.author == active_player)
            if move.content.strip().lower() == "exit":
                await ctx.send(active_player.mention + " gave up!")
                return
            try:
                move = int(move.content.strip().lower())
            except ValueError:
                await ctx.send("This doesn't look like a number")
                continue
            if move not in game.possible_moves():
                await ctx.send("You can't choose field " + str(move))
                continue
            game.make_move(move)
        winner = game.get_winner()
        await ctx.send(game.to_string())
        if winner == game.PLAYER:
            await ctx.send(opponent.mention + " won against " + challenger.mention)
        elif winner == game.COMPUTER:
            await ctx.send(challenger.mention + " won against " + opponent.mention)
        else:
            await ctx.send("It's a draw between " + challenger.mention + " and " + opponent.mention)


def setup(bot):
    bot.add_cog(TicTacToe(bot))
