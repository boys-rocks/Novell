import discord
from discord.ext import commands
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
#Random av command
class genav(commands.Cog):
  def __init__(self, bot):
        self.bot = bot
      
  @commands.command(help="Generate random av")
  async def genav(ctx, seed=None):
    if seed is None:
      seed = random.sample(string.ascii_letters, 5)
    async with aiohttp.ClientSession() as session:
      async with session.get(f"https://avatars.dicebear.com/api/micah/{seed}.svg?mood[]=happy") as resp:
        img_data = await resp.content.read()
    with open('img.svg', 'wb') as handler:
      handler.write(img_data)
    drawing = svg2rlg('img.svg')
    renderPM.drawToFile(drawing, 'img2.png', fmt='PNG')
    with open("img2.png", "rb") as fh:
      f = discord.File(fh, filename="av.png")
    await ctx.reply(file=f)
def setup(bot):
    bot.add_cog(genav(bot))
