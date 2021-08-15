
import discord
from discord.ext import commands
from gtts import gTTS 
from helpers import logHelper
import os
import random
import asyncio
def textVoice(myText): 
    myobj = gTTS(text=myText, lang='en', slow=False)   
# Saving the converted audio in a mp3 file
    myobj.save("soundfiles/tts.mp3") 
def randomSound(dir):
    listOfFiles = []
    for filename in os.listdir('./soundfiles/'+dir):
        listOfFiles.append(filename)
    chosenOne = random.choice(listOfFiles)  
    return "soundfiles/"+dir+"/"+chosenOne

def playNext(ctx, path):
    guild = ctx.message.guild
    voice_client = guild.voice_client
    print(path)
    voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: playNext(ctx, randomSound('chord')))
    voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)
    
def musicMaker(ctx):
    guild = ctx.message.guild
    voice_client = guild.voice_client
    path = randomSound('chord')
    print(path)
    voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: playNext(ctx, randomSound('chord')))
    voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)
    
    
    
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
    """Bot Audio Module"""
    def __init__(self, bot):
        self.bot = bot
    @commands.command(help="Definitely Doesn't Play Nyan Cat")
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
    @commands.command(help="Text-To-Speech Command")
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
    @commands.command(help="Plays random sound file from specified directory,\ntry *pog starwars or *pog animesounds")
    async def pog(self,ctx,dir):
            try: 
                data = await joinMusicChannel(ctx)
                if data == True:
                    guild = ctx.message.guild
                    voice_client = guild.voice_client
                    path = randomSound(dir)
                    print(path)
                    voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
                    voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)
            except Exception as e:
                logHelper.logger.warning(e)
    @commands.command(help="creates song from sound clips")
    async def song(self,ctx):
            try:    
                data = await joinMusicChannel(ctx)
                if data == True:
                    while True:
                        musicMaker(ctx)           
            except Exception as e:
                logHelper.logger.warning(e)
    @commands.command(help="tts from song lyrics or txt files")
    async def rap(self,ctx,dir): 
            try: 
                line = random.choice(open('textfiles/'+dir+'.txt').readlines())
                textVoice(line)
                data = await joinMusicChannel(ctx)
                if data == True:
                    guild = ctx.message.guild
                    voice_client = guild.voice_client
                    path = "soundfiles/tts.mp3"
                    print(path)
                    voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
                    voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)
            except Exception as e:
                logHelper.logger.warning(e)
def setup(bot):
    bot.add_cog(PlaySounds(bot))
