import discord
from discord.ext import commands
import requests

"""
merged chuckjokes insult, and programming jokes into this cog
"""
class Jokes(commands.Cog):
    "Collection of jokes, insults and affirmations"
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="NuubBot tells a Joke")
    async def joke(self, ctx):
        try:
            x = requests.get("https://official-joke-api.appspot.com/random_joke")
            await ctx.send(x.json()["setup"])
            await ctx.send(x.json()["punchline"])
        except Exception as ex:
            print("Exception", ex)
            
    @commands.command(help="Chuck Norris tells joke")
    async def chuckjokes(self, ctx):
        with requests.get(url=f"http://api.icndb.com/jokes/random") as response:
            await ctx.send(response.json()["value"]["joke"])
            
    @commands.command(help="Get insulted by NuubBot!")
    async def insult(self, ctx):
        with requests.get(
            url=f"https://evilinsult.com/generate_insult.php?lang=en&type=json"
        ) as response:
            await ctx.send(response.json()["insult"])


    @commands.command(help="NuubBot affirms you")
    async def affirm(self, ctx):
        try:
            x = requests.get("https://www.affirmations.dev/")
            await ctx.send(x.json()["affirmation"])
        except Exception as ex:
            print("Exception: ", ex)
    @commands.command(help="NuubBot tells a programming joke")
    async def projoke(self, ctx):
        with requests.get(
            url=f"https://v2.jokeapi.dev/joke/programming?type=single"
        ) as response:
            await ctx.send(response.json()["joke"])

def setup(bot):
    bot.add_cog(Jokes(bot))
