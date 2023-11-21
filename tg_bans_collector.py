from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
import pandas as pd


app = Client('me', 27836080, '70473ab2995b73e45b6e9c1992f2752e')

file = open('dataset.txt', 'a+')

@app.on_message()
def analyze(_, message: Message):
    text = message.text.lower()
    if 'ban' in text or 'бан' in text or 'mute' in text or 'мут' in text:
        try:
            bad_ = message.reply_to_message.text
            file.write(f'{bad_},1')
        except Exception as e:
            print(e)

app.run()   