from discord.ext import commands
from helpers.tic_tac_toe.tic_tac_toe_game import TicTacToeGame


class TicTacToe(commands.Cog):
    """
    Play Tic-Tac-Toe against the computer with three difficulties:
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
            # if move.content.strip().lower() == "exit":
            #     ctx.send("Exiting...")
            #     return
            # else:
            #     ctx.send("Not exiting")
            try:
                move = int(move.content.strip().lower())
            except ValueError:
                await ctx.send("This doesn't look like a number")
                continue
            if move not in game.possible_moves():
                await ctx.send("You can't choose field " + str(move))
                continue
            game.make_move(move)
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


def setup(bot):
    bot.add_cog(TicTacToe(bot))
