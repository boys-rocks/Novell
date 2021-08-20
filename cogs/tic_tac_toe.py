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
        await ctx.send(game.check_game_over())
        await ctx.send(game.check_draw())
        await ctx.send(game.check_winner(game.PLAYER))
        await ctx.send(game.check_winner(game.COMPUTER))
        while not game.check_game_over():
            move = await self.bot.wait_for(
                "message", check=lambda message: message.author == ctx.author).content.strip()
            if move.lower() == "exit":
                return
            try:
                move = int(move)
            except ValueError:
                await ctx.send("This doesn't look like a number")
                continue
            if move not in game.possible_moves():
                await ctx.send("You can't choose field " + str(move))
                continue
            game.make_move(move)
            await ctx.send(game.to_string())
            game.make_ai_move()
            await ctx.send(game.to_string(True))
            await ctx.send("Where do you want to go next")
        winner = game.get_winner()
        if winner == game.PLAYER:
            await ctx.send("You won! Congratulation!")
        elif winner == game.COMPUTER:
            await ctx.send("I won! Better luck next time!")
        else:
            await ctx.send("It's a Draw! Wanna play again?")


def setup(bot):
    bot.add_cog(TicTacToe(bot))
