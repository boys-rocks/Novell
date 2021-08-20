import discord
from helpers import emojis


def ask(message: str, who: discord.Member, channel: discord.abc.Messageable, bot: discord.ext.commands.Bot):
    request = await channel.send(message)
    await request.add_reaction(emojis.thumbsup)
    await request.add_reaction(emojis.thumbsdown)

    def check(_reaction: discord.Reaction, _user: discord.Member):
        return _reaction.message == request and _user == who
    while True:
        reaction, user = await bot.wait_for("reaction_add", check=check)
        if reaction.emoji == emojis.thumbsup:
            await request.delete(1)
            return True
        elif reaction.emoji == emojis.thumbsdown:
            await request.delete(1)
            return False
        else:
            reaction.remove()
