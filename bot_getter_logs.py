import twitchio as tio
from twitchio.ext import commands
import asyncio
import bot_config
import pymongo
import datetime as dt

def pre_bot_run():
    db = pymongo.MongoClient("mongodb://localhost:27017").jaba
    return db

class Bot(commands.Bot):
    def __init__(self, db):
        super().__init__(token=bot_config.TWITCH_TOKEN, prefix="JABA", initial_channels=['pwgood', 'poal48'])
        self.db = db

    async def event_ready(self):
        await self.get_channel("poal48").send(f"COPIUM JABA is now running | pomidor version | mongo db connected | {self.db.messages.count_documents({})} messages collected")
    
    async def event_message(self, message):
        if message.echo: return
        self.db.messages.insert_one({
            "time": dt.datetime.now().strftime("%H:%M:%S"),
            "channel": message.channel.name,
            "author": message.author.display_name,
            "test": message.content
        })
        await self.handle_commands(message=message)
    
    @commands.command(name="ping")
    async def command_ping(self, ctx: commands.Context):
        await ctx.reply(f"COPIUM JABA is running | pomidor verison | total messages: {self.db.messages.count_documents({})}")

    @commands.command(name="help")
    async def command_help(self, ctx: commands.Context):
        await ctx.reply("Бот работает в эксперементально-тестовом режиме. Весь функционал отключен. Пожалуйста, не спамьте этой командой 🥺")

db = pre_bot_run()
bot = Bot(db)
bot.run()