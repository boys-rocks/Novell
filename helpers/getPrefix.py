from pymongo import MongoClient
import os

MONGODB = os.environ.get("MONGODB", None)

client = MongoClient(MONGODB)
db = client["discord"]
collection = db["bot"]


async def getPrefix(bot, message):
    data = collection.find_one({"_id": message.guild.id})
    prefix = data["prefix"]
    return prefix
