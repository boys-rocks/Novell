import discord
from discord.ext import commands
import requests

class GitHub(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command('Get information on a github account')
    async def ghuser(self, ctx, *, user):
        x = requests.get(f'https://api.github.com/users/{user}')

        try:
            title = x.json()['login']
            link = x.json()['html_url']
            em = discord.Embed(title=title, description=f'[User Link]({link})')
            avatar_url = x.json()['avatar_url'] + '.png'
            em.set_thumbnail(url=avatar_url)
            em.add_field(name='Name', value=x.json()['name'])
            em.add_field(name='Company', value=x.json()['company'])
            em.add_field(name='Location', value=x.json()['location'])
            em.add_field(name='Hireable', value=x.json()['hireable'])
            em.add_field(name='Email', value=x.json()['email'])
            em.add_field(name='Bio', value=x.json()['bio'])
            em.add_field(name='Public Repos', value=x.json()['public_repos'])
            em.add_field(name='Followers', value=x.json()['followers'])
            em.add_field(name='Following', value=x.json()['following'])
            await ctx.send(embed=em)
        except Exception as ex:
            print('Exception:', ex)



def setup(bot):
    bot.add_cog(GitHub(bot))
