from pymongo import MongoClient

client = MongoClient("mongodb+srv://user:OzwrCJAoUJI78syX@cluster0.tsodk.mongodb.net/discord?retryWrites=true&w=majority")
db = client['discord']
collection = db['bot']

async def getPrefix(bot, message):
    data = collection.find_one({'_id': message.guild.id})
    prefix = data['prefix']
    return prefix