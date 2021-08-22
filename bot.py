import discord
from discord.ext import commands
from helpers.logHelper import logger
import os
import logging
from pymongo import MongoClient
from helpers.getPrefix import getPrefix
import ast
from helpers.getWeather import getLocationKey, getWeather
import time
from pretty_help import PrettyHelp
logging.basicConfig(level=logging.INFO)

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN", None)
MONGODB = os.environ.get("MONGODB", None)


bot = commands.Bot(command_prefix="*", help_command=PrettyHelp())
#bot = commands.Bot(command_prefix='*', help_command=None)

client = MongoClient(MONGODB)
db = client["discord"]
collection = db["bot"]

for filename in os.listdir('./cogs'):
    try:
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
            logger.info(f"Succesfully Loaded Cog: {filename}")
        else:
            print(f"Unable to load {filename}")
            logger.warning(
                f"Unable to load {filename}, is it suppose to be in cog directory?")
    except Exception as e:
        logger.warning(f"Unable to load cog: {e}")
"""
check for frequency data in mongo and create a doc for it if it doesnt exist
"""
if not collection.find_one({"_id": "word_command_freq"}):
    freq_data_exist = collection.find_one({"_id": "word_command_freq"})
    print(f"\n\n\n\nfreq data exist or na{freq_data_exist}\n\n\n")
    collection.insert_one({"_id": "word_command_freq"})
@bot.event
async def on_message(message):
    user = message.author
    contents = message.content.split(' ')
    word = contents[0]
    member = str(message.author)
    if user.bot:
        pass
    elif not word:
        print("no words to add")
    else:
        try:
            if "." in word:
                word = word.replace(".", "(Dot)")
            if "$" in word:
                word = word.replace("$", "(Dollar_Sign)")
        except Exception as e:
            print(str(e)+"Caught in on_message")
            logger.warning(e)
        print(member+": "+word)
        #is_in_word_command_freq=collection.find_one({"_id":"word_command_freq",word:{"$size": 0}})
        # print(is_in_word_command_freq)
        if collection.find_one({"_id": "word_command_freq", word: {"$exists": True}}):
            collection.update_one(
                {"_id": "word_command_freq"}, {"$inc": {word: 1}})
            print("incremented freq value " + word +
                  " by 1 in word_command_freq doc")
        else:
            print(collection.update(
                {"_id": "word_command_freq"}, {"$set": {word: 1}}))
            print("added " + word + " to word_command_freq")
        #print(collection.find_one({"_id": "word_command_freq"}))
    await bot.process_commands(message)


@bot.event
async def on_guild_join(guild):
    guild_id = guild.id
    collection.insert_one({'_id': guild_id, 'prefix': ','})
    print('done')


async def latency(ctx):
    time_1 = time.perf_counter()
    await ctx.trigger_typing()
    time_2 = time.perf_counter()
    ping = round((time_2 - time_1) * 1000)
    await ctx.send(f"ping = {ping}")

try:
    bot.run(DISCORD_TOKEN)
    logger.info("Bot Is Off\n----------------------------------- END OF SESSION")
except Exception as e:
    logger.warning(f"Bot Failed to initialise: {e}")