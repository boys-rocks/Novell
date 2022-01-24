import discord
from discord.ext import commands
import datetime
from random import choice


class Decisions(commands.Cog):
    "Polls and decision making commands"

    def __init__(self, bot):
        self.bot = bot

    @property
    def reactions(self):
        return {
            1: "1️⃣",
            2: "2️⃣",
            3: "3️⃣",
            4: "4️⃣",
            5: "5️⃣",
            6: "6️⃣",
            7: "7️⃣",
            8: "8️⃣",
            9: "9️⃣",
            10: "🔟",
        }

    @commands.command(help="Creates a simple poll with only 👍/👎 as an option.")
    async def ask(self, ctx, *, question: str) -> None:
        """
        creates  simple poll with only 👍/👎 as an option

        :param ctx: discord context manager
        :type ctx: discord.ContextManager
        :param question: question to poll on
        :type question: str
        """
        await ctx.message.delete()
        embed = discord.Embed(description=question)
        embed.set_author(
            name=f"Poll by {ctx.author.display_name}", icon_url=ctx.author.avatar_url
        )
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")

    @commands.Cog.listener()
    async def on_reaction(self, payload) -> None:
        """
        discord listener, reacts to people's reaction

        :param payload: discord message
        :type payload: discord.message
        """
        user = payload.member
        if user.bot:
            return
        msg = (
            await self.bot.get_guild(payload.guild_id)
            .get_channel(payload.channel_id)
            .fetch_message(payload.message_id)
        )
        emoji = payload.emoji
        users = []
        if msg.author.bot and ("👍" and "👎") in [str(i) for i in msg.reactions]:
            for react in msg.reactions:
                if str(react) == "👍":
                    async for reactor in react.users():
                        if reactor.bot:
                            continue
                        if reactor in users:
                            await msg.remove_reaction(emoji, user)
                            return
                        users.append(reactor)
                elif str(react) == "👎":
                    async for reactor in react.users():
                        if reactor.bot:
                            continue
                        if reactor in users:
                            await msg.remove_reaction(emoji, user)
                            return
                    return

#HISTORY: POLL CMD WAS HERE

    @commands.command(help="toss a coin")
    async def toss(self, ctx) -> None:
        """
        toss a coin

        :param ctx: discord context manager
        :type ctx: discord.ContextManager
        """
        await ctx.send(f"Coin is tossed, and.... it's {choice(['HEADS','TAILS'])}")

    @commands.command(help="takes a decision from available choices")
    async def choose(self, ctx, *args) -> None:
        """
        choose one the given option

        :param ctx: discord context manager
        :type ctx: discord.ContextManager
        """
        respose = choice(
            ["choose", "prefer", "think you should go with", "would choose"]
        )
        await ctx.send(f"Well! , I {respose} {choice(args)}")


def setup(bot):
    bot.add_cog(Decisions(bot))
