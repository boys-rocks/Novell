import discord
from discord.ext import commands
import datetime
from random import choice
from requests.models import Response
"""
merged choose cog into this cog
"""
class Helpful(commands.Cog):
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

    @commands.command(help="Create a poll")
    async def poll(self, ctx, *, suggestion):
        await ctx.message.delete()
        embed = discord.Embed(description=suggestion)
        embed.set_author(
            name=f"Poll by {ctx.author.display_name}", icon_url=ctx.author.avatar_url
        )
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")

    @commands.Cog.listener()
    async def on_reaction(self, payload):
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

    @commands.command(help = "Multi Choice Polls")
    async def multi_choice(self, ctx, desc, *choices):
        await ctx.message.delete()

        if len(choices) < 2:
            ctx.command.reset_cooldown(ctx)
            if len(choices) == 1:
                return await ctx.send("Can't make a poll with only one choice")
            return await ctx.send(
                "You have to enter two or more choices to make a poll"
            )

        if len(choices) > 10:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send("You can't make a poll with more than 10 choices")

        embed = discord.Embed(
            description=f"**{desc}**\n\n"
            + "\n\n".join(
                f"{str(self.reactions[i])}  {choice}"
                for i, choice in enumerate(choices, 1)
            ),
            timestamp=datetime.datetime.utcnow(),
            color=discord.colour.Color.gold(),
        )
        embed.set_footer(text=f"Poll by {str(ctx.author)}")
        msg = await ctx.send(embed=embed)
        for i in range(1, len(choices) + 1):
            await msg.add_reaction(self.reactions[i])
    @commands.command(help="Coin toss command")
    async def toss(self, ctx):
        await ctx.send(f"Coin is tossed, and.... it's {choice(['HEADS','TAILS'])}")

    @commands.command(help="Make a decision for you command")
    async def choose(self, ctx, *args):
        respose = choice(
            ["choose", "prefer", "think you should go with", "would choose"]
        )
        await ctx.send(f"Well! , I {respose} {choice(args)}")


def setup(client):
    client.add_cog(Helpful(client))
