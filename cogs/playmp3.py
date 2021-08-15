from asyncio.futures import _set_result_unless_cancelled
import discord
from discord.ext import commands
from gtts import gTTS 
from helpers import logHelper
import os
import asyncio
def textVoice(myText): 
    myobj = gTTS(text=myText, lang='en', slow=False)   
# Saving the converted audio in a mp3 file
    myobj.save("soundfiles/tts.mp3") 
async def joinMusicChannel(ctx):
    try:
        channel = ctx.author.voice.channel
    except:
        await ctx.send(ctx.author.mention + " Please join the music voice channel.")
        return False

    vc = ctx.voice_client
    if vc == None:
        await channel.connect()
    return True

def endSong(guild, path):
    pass
class PlaySounds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def nyan(self,ctx):
        try:
            data = await joinMusicChannel(ctx)
            if data == True:
                guild = ctx.message.guild
                voice_client = guild.voice_client
                path = "soundfiles/Nyan.mp3"
                voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
                voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)
        except Exception as e:
            logHelper.logger.warning(e)
    @commands.command()
    async def tts(self,ctx,*args):
        try:
            joinedSentence= ' '.join(map(str, args))
            textVoice(joinedSentence)
            data = await joinMusicChannel(ctx)
            if data == True:
                guild = ctx.message.guild
                voice_client = guild.voice_client
                path = "soundfiles/tts.mp3"
                voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
                voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)
        except Exception as e:
            logHelper.logger.warning(e)
def setup(bot):
    bot.add_cog(PlaySounds(bot))