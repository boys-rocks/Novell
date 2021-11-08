import discord
from discord.ext import commands


class Board(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="info_board", aliases=["b", "showboard"])
    async def info_board(self, ctx):
        """
        Displays the current board.
        **board supports use of markdown
        """

        try:
            with open("board.txt", "r") as f:
                board = f.read()
                await ctx.send(board)
        except FileNotFoundError:
            await ctx.send("The board is empty.")
        except:
            await ctx.send("Something went wrong.")

    @commands.has_role("Admin")
    @commands.command(name="add", aliases=["a"])
    async def add(self, ctx, *, info):
        """
        Adds a info to the board.
        """
        try:
            with open("board.txt", "a") as f:
                f.write(f"{info}\n")
                await ctx.send("Added to the board.")
        except FileNotFoundError:
            with open("board.txt", "w") as f:
                f.write(f"{info}\n")
                await ctx.send("Added to the board.")
        except discord.Forbidden:
            await ctx.send("I don't have permission to add to the board.")
        except:
            await ctx.send("Something went wrong.")

    @commands.has_role("Admin")
    @commands.command(name="remove", aliases=["r"])
    async def remove(self, ctx, *, info):
        """
        Removes a info from the board.
        """
        try:
            with open("board.txt", "r") as f:
                board = f.readlines()
                board = [x.strip() for x in board]
                if info in board:
                    board.remove(info)
                    with open("board.txt", "w") as f:
                        for line in board:
                            f.write(f"{line}\n")
                        await ctx.send("Removed from the board.")
                else:
                    await ctx.send("That info is not on the board.")
        except FileNotFoundError:
            await ctx.send("The board is empty.")
        except:
            await ctx.send("Something went wrong.")

    @commands.has_role("Admin")
    @commands.command(name="clear", aliases=["c", "wipe"])
    async def clear(self, ctx):
        """
        Clears the board.
        """
        try:
            with open("board.txt", "w") as f:
                f.write("")
                await ctx.send("The board has been cleared.")
        except FileNotFoundError:
            await ctx.send("The board is empty.")
        except:
            await ctx.send("Something went wrong.")

    @commands.has_role("Admin")
    @commands.command(name="edit", aliases=["e"])
    async def edit(self, ctx, *, info):
        """
        Edits a info on the board.
        """
        try:
            with open("board.txt", "r") as f:
                board = f.readlines()
                board = [x.strip() for x in board]
                if info in board:
                    board.remove(info)
                    with open("board.txt", "w") as f:
                        for line in board:
                            f.write(f"{line}\n")
                        await ctx.send("Removed from the board.")
                else:
                    await ctx.send("That info is not on the board.")
        except FileNotFoundError:
            await ctx.send("The board is empty.")
        except:
            await ctx.send("Something went wrong.")


def setup(bot):
    bot.add_cog(Board(bot))
