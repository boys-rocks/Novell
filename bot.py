import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from helpers import logHelper
from gtts import gTTS
import os
import logging
logging.basicConfig(level=logging.INFO)
os.sys.path.append('/ffmpeg/bin')

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN", None)

bot = commands.Bot(command_prefix=",", help_command=None)
 
for filename in os.listdir('./cogs'):
    try:
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
            logHelper.logger.info(f"Succesfully Loaded Cog: {filename}")
        else:
            print(f"Unable to load {filename}")
            logHelper.logger.warning(f"Unable to load {filename}, is it suppose to be in cog directory?")
    except Exception as e:
        logHelper.logger.warning(f"Unable to load cog: {e}")
try:
    bot.run(DISCORD_TOKEN)
    logHelper.logger.info("Bot Is Off\n----------------------------------- END OF SESSION")
except Exception as e:
    logHelper.logger.warning(f"Bot Failed to initialise: {e}")

