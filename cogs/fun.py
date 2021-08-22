import discord
from discord.ext import commands
import requests
import random

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

    @commands.command()
    async def pypi(self,ctx,*,package):
        try:
            x = requests.get(f'https://pypi.python.org/pypi/{package}/json')
            x = x.json()
            pauthor = x['info']['author']
            em = discord.Embed(title=x['info']['name'], description = f'By {pauthor}')
            url = x['info']['package_url']
            em.add_field(name='URL', value= f'[Link]({url})',inline=True)
            
            em.add_field(name='Email', value=x['info']['author_email'],inline=True)
            em.add_field(name='Home page', value=x['info']['home_page'],inline=True)
            em.add_field(name='License', value=x['info']['license'],inline=True)
            url = x['info']['package_url']

            await ctx.send(embed=em)
        except Exception as ex:
            print('Exception: ', ex)

    @commands.command()
    async def cat(self,ctx):
        x = requests.get('https://api.thecatapi.com/v1/images/search')
        imageurl = x.json()[0]['url']
        em = discord.Embed(title='Cat?')
        em.set_image(url=imageurl)
        await ctx.send(embed=em)

    @commands.command()
    async def meme(self, ctx):
        x = requests.get('https://meme-api.herokuapp.com/gimme').json()
        embed = discord.Embed(title=x['title'])
        url = x['url']
        embed.set_image(url=url)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Fun(bot))
