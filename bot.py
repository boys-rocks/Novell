import discord
from discord.ext import commands


bot = commands.Bot(command_prefix=',', help_command=None)


@bot.event
async def on_ready():
    print('Ready..')
    print('Logged in as: ', bot.user)
    print('Prefix: ', bot.command_prefix)
    print('Latency: ', bot.latency)


@bot.command()
async def help(ctx):
    await ctx.send('there is supposed to be a help command here.')

bot.run('ODc1NTcxODQ3Njc1MTUwMzc2.YRXd0w.R2brla6u5MjfCvuL6whMXxT9gXY')