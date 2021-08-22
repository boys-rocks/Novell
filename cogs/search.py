import discord
from discord.ext import commands
import wikipedia
import requests


class Search(commands.Cog):
    "Module to search Wikipedia, Github, and pypi"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Searches wikipedia")
    async def search(self, ctx, *query):
        sentence = " ".join(query)
        result = wikipedia.summary(sentence, sentences=2)
        await ctx.send(result)

    @commands.command(help="Search for information on a github account")
    async def ghuser(self, ctx, *, user):
        x = requests.get(f"https://api.github.com/users/{user}")

        try:
            title = x.json()["login"]
            link = x.json()["html_url"]
            em = discord.Embed(title=title, description=f"[User Link]({link})")
            avatar_url = x.json()["avatar_url"] + ".png"
            em.set_thumbnail(url=avatar_url)
            em.add_field(name="Name", value=x.json()["name"])
            em.add_field(name="Company", value=x.json()["company"])
            em.add_field(name="Location", value=x.json()["location"])
            em.add_field(name="Hireable", value=x.json()["hireable"])
            em.add_field(name="Email", value=x.json()["email"])
            em.add_field(name="Bio", value=x.json()["bio"])
            em.add_field(name="Public Repos", value=x.json()["public_repos"])
            em.add_field(name="Followers", value=x.json()["followers"])
            em.add_field(name="Following", value=x.json()["following"])
            await ctx.send(embed=em)
        except Exception as ex:
            print("Exception:", ex)

    @commands.command(help="Search for information on a github repository")
    async def ghrepo(self, ctx, user, *, repo):
        try:
            x = requests.get(f"https://api.github.com/repos/{user}/{repo}")
            x = x.json()
            title = x["full_name"]
            id0 = x["id"]
            url1 = x["html_url"]
            em = discord.Embed(title=f"[{title}]({url1}) ({id0})", description=f"")
            owner1 = x["owner"]["login"]
            owner2 = x["owner"]["html_url"]
            typez = x["owner"]["type"]
            em.add_field(name="Owner", value=f"[{owner1}]({owner2}), Type: {typez}")
            em.add_field(name="Private", value=x["private"])
            desc = x["description"]
            em.add_field(name="Descritpion", value=desc)
            em.add_field(name="Fork", value=x["fork"])
            em.add_field(name="Language(s)", value=x["language"])
            em.add_field(name="Forks Count", value=x["forks_counts"])
            em.add_field(name="License", value=x["license"]["name"])
            image_url = x["owner"]["avatar_url"]
            em.set_thumbnail(url=image_url)
        except Exception as ex:
            print("Exception: ", ex)

    @commands.command(help="Search for pypi package info")
    async def pypi(self, ctx, *, package):
        try:
            x = requests.get(f"https://pypi.python.org/pypi/{package}/json")
            x = x.json()
            pauthor = x["info"]["author"]
            em = discord.Embed(title=x["info"]["name"], description=f"By {pauthor}")
            url = x["info"]["package_url"]
            em.add_field(name="URL", value=f"[Link]({url})", inline=True)

            em.add_field(name="Email", value=x["info"]["author_email"], inline=True)
            em.add_field(name="Home page", value=x["info"]["home_page"], inline=True)
            em.add_field(name="License", value=x["info"]["license"], inline=True)
            url = x["info"]["package_url"]

            await ctx.send(embed=em)
        except Exception as ex:
            print("Exception: ", ex)


def setup(bot):
    bot.add_cog(Search(bot))
