import discord
from discord.ext import commands
#Cat, Dog, and Awwbomb command
class animals(commands.Cog):
  def __init__(self, bot):
        self.bot = bot    
  @commands.command(help="Picture of Cat")
  async def cat(ctx):
    catmbed = discord.Embed(title="oOo a Cat!")
    async with aiohttp.ClientSession() as sesh:
      async with sesh.get('https://www.reddit.com/r/cat/new.json?sort=hot') as resp:
        res = await resp.json()
     try:
        catmbed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
     except:
        catmbed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
     await ctx.reply(embed=catmbed
  @commands.command(help="Picture of Dog")
  async def cat(ctx):
      catmbed = discord.Embed(title="oOo a Dog!")
      async with aiohttp.ClientSession() as sesh:
        async with sesh.get('https://www.reddit.com/r/dog/new.json?sort=hot') as resp:
          res = await resp.json()
      try:
        catmbed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
      except:
        catmbed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
      await ctx.reply(embed=catmbed
  @commands.command(help="5 pictures of dogs and cats \:D")
  async def awwbomb(ctx):
    async with sesh.get('https://www.reddit.com/r/dog/new.json?sort=hot') as resp:
        res = await resp.json()
    for x in range(0,5):
        await ctx.reply(f"{res['data']['children'] [random.randint(0, 25)]['data']['url']}")
def setup(bot):
    bot.add_cog(animals(bot))
