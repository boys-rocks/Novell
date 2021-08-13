import discord
from discord.ext import commands
import os

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN", None)

bot = commands.Bot(command_prefix=",", help_command=None)


@bot.event
async def on_ready():
    print('Ready..')
    print('Logged in as: ', bot.user)
    print('Prefix: ', bot.command_prefix)
    print('Latency: ', round(bot.latency*1000), 'ms')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
        else:
            print(f"Unable to load {filename}")


@bot.command()
async def ping(ctx):
    em = discord.Embed(title='Pong!', description=f'{round(bot.latency * 100)} ms')
    await ctx.send(embed=em)


@bot.command()
async def help(ctx):
    await ctx.send("there is supposed to be a help command here.")


bot.run(DISCORD_TOKEN)
