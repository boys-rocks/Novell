import discord
from discord.ext import commands
from helpers.logHelper import logger
import os
import logging
from pymongo import MongoClient
from pretty_help import PrettyHelp

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN", None)
MONGODB = os.environ.get("MONGODB", None)

logging.basicConfig(level=logging.INFO)
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(
    command_prefix="nv.",
    help_command=PrettyHelp(),
    intents=intents,
    case_insensitive=True,
)

client = MongoClient(MONGODB)
db = client["discord"]
collection = db["bot"]


all_categories = [category for category in os.listdir("./cogs")]
for category in all_categories:
    print(f"Loading cogs from : {category} ................\n")
    for filename in os.listdir(f"./cogs/{category}"):
        try:
            if filename.endswith(".py"):
                bot.load_extension(f"cogs.{category}.{filename[:-3]}")
                logger.info(f"Successfully Loaded Cog: {filename}")
            else:
                print(f"Unable to load {filename}")
                logger.warning(
                    f"Unable to load {filename}, is it suppose to be in cog directory?"
                )
        except Exception as e:
            logger.warning(f"Unable to load cog: {e}")
bot.load_extension("jishaku")


"""
check for frequency data in mongo and create a doc for it if it doesn't exist
"""
if not collection.find_one({"_id": "word_command_freq"}):
    freq_data_exist = collection.find_one({"_id": "word_command_freq"})
    collection.insert_one({"_id": "word_command_freq"})
if not collection.find_one({"_id": "paper_trading_accounts"}):
    freq_data_exist = collection.find_one({"_id": "paper_trading_accounts"})
    collection.insert_one({"_id": "paper_trading_accounts"})


@bot.event
async def on_message(message):
    user = message.author
    contents = message.content.split(" ")
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
            print(str(e) + "Caught in on_message")
            logger.warning(e)
        print(member + ": " + word)
        # is_in_word_command_freq=collection.find_one({"_id":"word_command_freq",word:{"$size": 0}})
        # print(is_in_word_command_freq)
        if collection.find_one({"_id": "word_command_freq", word: {"$exists": True}}):
            collection.update_one({"_id": "word_command_freq"}, {"$inc": {word: 1}})
            print("incremented freq value " + word + " by 1 in word_command_freq doc")
        else:
            print(collection.update({"_id": "word_command_freq"}, {"$set": {word: 1}}))
            print("added " + word + " to word_command_freq")
        # print(collection.find_one({"_id": "word_command_freq"}))
    await bot.process_commands(message)


@bot.event
async def on_guild_join(guild):
    guild_id = guild.id
    collection.insert_one({"_id": guild_id, "prefix": ","})
    print("done")


# cookies

try:
    bot.run(DISCORD_TOKEN)
    logger.info("Bot Is Off\n----------------------------------- END OF SESSION")
except Exception as e:
    logger.warning(f"Bot Failed to initialise: {e}")
