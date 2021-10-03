import discord
from discord.ext import commands
import akinator as ak
import asyncio


class Akinator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["aki"])
    async def akinator(self, ctx):
        """
        Akinator is a video game developed by French company Elokence. During gameplay, it attempts to determine what fictional or real-life character the player is thinking of by asking a series of questions.

        :param ctx: discord context manager
        :type ctx: discord.ContextManager
        """
        intro = discord.Embed(
            title="Akinator",
            description="Hello, " + ctx.author.mention + "I am Akinator!!!",
            color=discord.Colour.green(),
        )
        intro.set_thumbnail(url="https://i.imgur.com/FSKqySm.png")
        intro.set_footer(
            text="Think about a real or fictional character.\n I will try to guess who it is.\ntype `start` to start."
        )
        outro = discord.Embed(
            title="Akinator",
            description="Bye, " + ctx.author.mention,
            color=discord.Colour.red(),
        )
        outro.set_footer(text="Akinator left the chat!!")
        outro.set_thumbnail(url="https://i.imgur.com/ElCDSb2.png")
        await ctx.send(embed=intro)

        def check(msg):
            return (
                msg.author == ctx.author
                and msg.channel == ctx.channel
                and msg.content.lower()
                in [
                    "y",
                    "n",
                    "p",
                    "b",
                    "yes",
                    "no",
                    "probably",
                    "idk",
                    "back",
                    "q",
                    "quit",
                    "exit",
                ]
            )

        try:
            aki = ak.Akinator()
            q = aki.start_game()
            while aki.progression <= 80:
                question = discord.Embed(
                    title="Question", description=q, color=discord.Colour.green()
                )
                question.set_thumbnail(url="https://i.imgur.com/x4WKztO.jpg")
                question.set_footer(text="Your answer:`[y/n/p/idk/b, q]`")
                question_sent = await ctx.send(embed=question)
                try:
                    msg = await self.bot.wait_for("message", check=check, timeout=30)
                except asyncio.TimeoutError:
                    await question_sent.delete()
                    await ctx.reply(
                        "`sorry you took too long to respond!\n(waited for `30sec`)`"
                    )
                    await ctx.send(embed=outro)
                    return
                await question_sent.delete()
                if msg.content.lower() in ["b", "back"]:
                    try:
                        q = aki.back()
                    except ak.CantGoBackAnyFurther as e:
                        await ctx.send(e)
                        continue
                elif msg.content.lower() in ["exit", "quit", "q"]:
                    await msg.delete()
                    return
                else:
                    try:
                        q = aki.answer(msg.content.lower())
                    except ak.InvalidAnswerError as e:
                        await ctx.send(e)
                        continue
                await msg.delete()
            aki.win()
            answer = discord.Embed(
                title=aki.first_guess["name"],
                description=aki.first_guess["description"],
                color=discord.Colour.green(),
            )
            answer.set_thumbnail(url=aki.first_guess["absolute_picture_path"])
            answer.set_image(url=aki.first_guess["absolute_picture_path"])
            answer.set_footer(text="`was I correct? : (y/n)`")
            await ctx.send(embed=answer)
            try:
                correct = await self.bot.wait_for("message", check=check, timeout=30)
            except asyncio.TimeoutError:
                await ctx.reply(
                    "`sorry you took too long to respond! (waited for 30sec)`"
                )
                await ctx.reply(embed=outro)
                return
            if correct.content.lower() == "y":
                yes = discord.Embed(title="Yeah!!!", color=discord.Colour.green())
                yes.set_thumbnail(url="https://imgur.com/LnrlJcb.png")
                await ctx.reply(embed=yes)
            else:
                no = discord.Embed(title="Oh Noooooo!!!", color=discord.Colour.red())
                no.set_thumbnail(url="https://i.imgur.com/ZNGFLD9.png")
                await ctx.reply(embed=no)
            await ctx.reply(embed=outro)
        except Exception as e:
            await ctx.send(e)


def setup(bot):
    bot.add_cog(Akinator(bot))
