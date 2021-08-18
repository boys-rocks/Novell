import discord
from discord.ext import commands
from discord.ext.commands import *
from pymongo import MongoClient
import asyncio
import os

MONGODB = os.environ.get('MONGODB', None)

client = MongoClient(MONGODB)
db = client['discord']
collection = db['bot']


class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_message')
    async def on_message(self, message):
        return await self.afkcheck(message)

    @commands.Cog.listener('on_message')
    async def on_message2(self, message):
        list1 = message.raw_mentions
        for i in list1:
            try:
                results = collection.find_one({'_id':'afk'})
                word = str(i)
                embed=discord.Embed(title='Member currently AFK:',description=results[word],color=discord.Color.random())
                await message.channel.send(embed=embed)
            except Exception as ex:
                print('Exception: ', ex)

    @commands.command()
    async def afk(self, ctx, *, reason='AFK'):
        await self.afkcommand(ctx, reason)

    async def afkcommand(self, ctx, reason):
        try:
            await ctx.author.edit(nick=f'[AFK] {ctx.message.author}')
        except Exception as ex:
            print('Exception: ', ex)
        try:
            collection.update_one({'_id': 'afk'}, {'$set':{str(ctx.author.id): reason}})
            embed=discord.Embed(title='AFK set:', description=reason,color=discord.Color.random())
            await ctx.send(embed=embed)
            await asyncio.sleep(10)
            collection.update_one({'_id': 'afk'}, {'$set': {f'k{str(ctx.author.id)}': '10'}})
        except Exception as ex:
            print(ex)
        


    async def afkcheck(self, message):
        if message.author.bot:
            return
        else:
            results = collection.find_one({'_id':'afk'})
            try:
                if results[str(message.author.id)] != None:
                    try:
                        await message.author.edit(nick=None)
                    except Exception as ex:
                        print('Exception: ', ex)

                    try:
                        if results[str(f'k{message.author.id}')] == '10':
                            collection.update_one({'_id':'afk'},{'$unset':{str(message.author.id):''}})
                            collection.update_one({'_id':'afk'},{'$unset':{f'k{str(message.author.id)}':''}})
                            embed=discord.Embed(title='Welcome back',description='Removed the AFK.',color=discord.Color.random())
                            await message.channel.send(embed=embed)
                    except Exception as ex:
                        print(ex)
            except Exception as ex:
                pass

def setup(bot):
    bot.add_cog(AFK(bot))
