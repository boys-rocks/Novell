import discord
from discord.ext import commands
import requests
import random
import aiohttp


class Bored(commands.Cog):
    "Fun Commands Module for bored times."

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Get an activity")
    async def activity(self, ctx) -> None:
        """
        suggests a random activity.
        """

        x = requests.get("https://www.boredapi.com/api/activity")
        await ctx.send(
            embed=discord.Embed(
                title=x.json()["activity"], description=x.json()["type"]
            )
        )

    @commands.command(help="Predict which country a name is from")
    async def name(self, ctx, *, name: str) -> None:
        """
        predicts the nationality of a person given their name.
        :param name: name to search for
        :type name: str
        """
        y = requests.get(f"https://api.nationalize.io?name={name}")
        result = y.json()["country"][0]["country_id"]
        await ctx.send(f"Your name is likely from {result}")

    @commands.command(help="Get information on a country")
    async def country(self, ctx, *, name: str) -> None:
        """
        Get information about countries

        :param name: name of the country
        :type name: str
        """
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

    @commands.command(help="Cat image command")
    async def cat(self, ctx) -> None:
        """
        sends cat images

        """
        x = requests.get("https://api.thecatapi.com/v1/images/search")
        imageurl = x.json()[0]["url"]
        em = discord.Embed(title="Cat?")
        em.set_image(url=imageurl)
        await ctx.send(embed=em)

    @commands.command(help="Picture of Dog")
    async def dog(self, ctx) -> None:
        """
        sends dog images

        """
        catmbed = discord.Embed(title="oOo a Dog!")
        async with aiohttp.ClientSession() as sesh:
            async with sesh.get(
                "https://www.reddit.com/r/DOG/new.json?sort=hot"
            ) as resp:
                res = await resp.json()
            try:
                catmbed.set_image(
                    url=res["data"]["children"][random.randint(0, 25)]["data"]["url"]
                )
            except:
                catmbed.set_image(
                    url=res["data"]["children"][random.randint(0, 25)]["data"]["url"]
                )
            await ctx.reply(embed=catmbed)

    @commands.command(help="5 pictures of dogs and cats")
    async def awwbomb(self, ctx) -> None:
        """
        send 5 random dog and cats images

        """
        async with aiohttp.ClientSession() as sesh:
            async with sesh.get(
                "https://www.reddit.com/r/dog/new.json?sort=hot"
            ) as resp:
                res = await resp.json()
            for x in range(0, 5):
                await ctx.send(
                    f"{res['data']['children'] [random.randint(0, 25)]['data']['url']}"
                )

    @commands.command(help="Get Quizzed on trivia questions!")
    async def trivia(self, ctx) -> None:
        """
        sends a random trivia question

        """
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
    async def meme(self, ctx) -> None:
        """
        sends a random meme

        """
        x = requests.get("https://meme-api.herokuapp.com/gimme").json()
        embed = discord.Embed(title=x["title"])
        url = x["url"]
        embed.set_image(url=url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Bored(bot))
