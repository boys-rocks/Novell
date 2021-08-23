import discord
from discord.ext import commands
import requests


class Bored(commands.Cog):
    "Fun Commands Module"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Get an activity")
    async def activity(self, ctx):
        import requests

        x = requests.get("https://www.boredapi.com/api/activity")
        await ctx.send(
            embed=discord.Embed(
                title=x.json()["activity"], description=x.json()["type"]
            )
        )

    @commands.command(help="Predict which country a name is from")
    async def name(self, ctx, *, name):
        y = requests.get(f"https://api.nationalize.io?name={name}")
        result = y.json()["country"][0]["country_id"]
        await ctx.send(f"Your name is likely from {result}")

    @commands.command(help="Get information on a country")
    async def country(self, ctx, *, name):
        x = requests.get(f"https://restcountries.eu/rest/v2/name/{name}?fullText=true")
        y = x.json()[0]
        em = discord.Embed(title=name)
        code1 = y["alpha2Code"]
        code2 = y["alpha3Code"]
        em.add_field(name="Country Code:", value=f"{code1}, {code2}")
        callcode = y["callingCodes"][0]
        em.add_field(name="Call Code:", value=f"{callcode}")
        capital = y["capital"]
        em.add_field(name="Capital:", value=f"{capital}")
        region1 = y["subregion"]
        region2 = y["region"]
        em.add_field(name="Regions:", value=f"{region1}, {region2}")
        currency = y["currencies"][0]["code"]
        currency2 = y["currencies"][0]["name"]
        em.add_field(name="Currency:", value=f"{currency}, {currency2}")
        language = y["languages"][0]["name"]
        em.add_field(name="Languages:", value=f"{language}")
        flag = f"https://www.countryflags.io/{code1}/flat/64.png"
        em.set_thumbnail(url=flag)
        await ctx.send(embed=em)

    # put pypi search in search cog

    @commands.command(help="Cat image command")
    async def cat(self, ctx):
        x = requests.get("https://api.thecatapi.com/v1/images/search")
        imageurl = x.json()[0]["url"]
        em = discord.Embed(title="Cat?")
        em.set_image(url=imageurl)
        await ctx.send(embed=em)

    @commands.command(help="Get Quizzed on trivia questions!")
    async def trivia(self, ctx):
        with requests.get(url=f"http://jservice.io/api/random") as response:
            answer = response.json()[0]["answer"]
            await ctx.send(response.json()[0]["question"])
            guess = await self.bot.wait_for(
                "message", check=lambda message: message.author == ctx.author
            )
            if guess.content.lower() == answer.lower():
                await ctx.send(
                    f"You are correct ✓✓. {guess.content.lower()} is the right answer"
                )
            else:
                await ctx.send(f"Incorrect ✗✗. Correct answer is {answer.lower()} ")

    @commands.command(help="Get a free meme XD")
    async def meme(self, ctx):
        x = requests.get("https://meme-api.herokuapp.com/gimme").json()
        embed = discord.Embed(title=x["title"])
        url = x["url"]
        embed.set_image(url=url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Bored(bot))
