import discord
from discord.ext import commands
import requests


class Fun(commands.Cog):
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

    @commands.command(help='Get information on a country')
    async def country(self, ctx, *, name):
        x = requests.get(f'https://restcountries.eu/rest/v2/name/{name}?fullText=true')
        y = x.json()[0]
        em = discord.Embed(title=name)
        code1 = y['alpha2Code']
        code2 = y['alpha3Code']
        em.add_field(name='Country Code:', value=f'{code1}, {code2}')
        callcode = y['callingCodes'][0]
        em.add_field(name='Call Code:', value=f'{callcode}')
        capital = y['capital']
        em.add_field(name='Capital:', value=f'{capital}')
        region1 = y['subregion']
        region2 = y['region']
        em.add_field(name='Regions:', value=f'{region1}, {region2}')
        currency = y['currencies'][0]['code']
        currency2 = y['currencies'][0]['name']
        em.add_field(name='Currency:', value=f'{currency}, {currency2}')
        language = y['languages'][0]['name']
        em.add_field(name='Languages:', value=f'{language}')
        flag = f'https://www.countryflags.io/{code1}/flat/64.png'
        em.set_thumbnail(url=flag)
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Fun(bot))
