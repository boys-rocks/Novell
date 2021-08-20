import discord
from discord.ext import commands
from helpers.logHelper import logger
import os
import logging
from pymongo import MongoClient
from helpers.getPrefix import getPrefix
import ast
from helpers.getWeather import getLocationKey, getWeather



logging.basicConfig(level=logging.INFO)
os.sys.path.append('/ffmpeg/bin')

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN", None)
MONGODB = os.environ.get("MONGODB", None)

bot = commands.Bot(command_prefix='ch.', help_command=None)

client = MongoClient(MONGODB)
db = client['discord']
collection = db['bot']
 
for filename in os.listdir('./cogs'):
    try:
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
            logger.info(f"Succesfully Loaded Cog: {filename}")
        else:
            print(f"Unable to load {filename}")
            logger.warning(f"Unable to load {filename}, is it suppose to be in cog directory?")
    except Exception as e:
        logger.warning(f"Unable to load cog: {e}")
      
@bot.event
async def on_guild_join(guild):
    guild_id = guild.id
    collection.insert_one({"_id": guild_id, "prefix": ","})
    print("done")


async def latency(ctx):
   time_1 = time.perf_counter()
   await ctx.trigger_typing()
   time_2 = time.perf_counter()
   ping = round((time_2-time_1)*1000)
   await ctx.send(f"ping = {ping}")


@bot.command(help = "Chage prefix command, Refactor into base cog?")
async def prefix(ctx, prefix):
    collection.update_one({"_id": ctx.guild.id}, {"$set": {"prefix": prefix}})
    await ctx.send(embed=discord.Embed(title="Updated Prefix: ",
                                       description=f"New prefix: {prefix}"))

@bot.command("Help command in bot.py file, refactor into help cog?")
async def helpv1(ctx):
    docstring_values = await __parse_docstrings()
    caller_message = ctx.message.content
    if len(caller_message.split()) == 1:
        # The message which called the help command has no params
        message_text = "Available Commands:\n```\n"
        for cog in docstring_values.keys():
            message_text += f"* {cog}"
        message_text += "\n```"
        await ctx.send(message_text)
    else:
        # The command has parameters, search for cog with required name
        cog = caller_message.split()[1]
        try:
            em = discord.Embed()
            em.add_field(name="name", value=cog, inline=False)
            for key, value in docstring_values[cog].items():
                em.add_field(name=key, value=value, inline=False)
            await ctx.send(embed=em)
        except:
            em = discord.Embed(title="Error",
                               description=f"Could not find command {cog}")
            await ctx.send(embed=em)

@bot.command()
async def check(ctx):
    await ctx.send('success')


async def __parse_docstring(filename):
    with open(filename, "r") as f:
        contents = f.read()
    module = ast.parse(contents)
    docstring = ast.get_docstring(module)
    if not docstring:
        docstring = "description: <Unknown>\n" + "syntax: <Unknown>"
    return {
        line.split(": ")[0]: "".join(line.split(": ")[1:])
        for line in docstring.split("\n") if line.strip()
    }


async def __parse_docstrings():
    values = {}
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            values[filename.strip(".py")] = await __parse_docstring(
                os.path.join("cogs", filename))
    return values
try:
    bot.run('ODc3MTYzMjA4Nzk5MDUxODA2.YRun5Q.DaA5GGVEyVZ2tc7qaMT2zzPmbuY')
    logger.info("Bot Is Off\n----------------------------------- END OF SESSION")
except Exception as e:
    logger.warning(f"Bot Failed to initialise: {e}")

