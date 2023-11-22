import twitchio as tio
from twitchio.ext import commands
import asyncio
import bot_config
import datetime as dt
import tensorflow as tf
import json
import numpy as np

def generate_text(model, start_string, temp, gen_chars, vocab):     
  char2idx = {u:i for i, u in enumerate(vocab)}
  idx2char = np.array(vocab)
  input_eval = [char2idx[s] for s in start_string]
  input_eval = tf.expand_dims(input_eval, 0)  
  text_generated = []
  model.reset_states()
  for i in range(gen_chars):
    predictions = model(input_eval)      
    predictions = tf.squeeze(predictions, 0)
    predictions = predictions / temp
    predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()
    input_eval = tf.expand_dims([predicted_id], 0)
    text_generated.append(idx2char[predicted_id])  
  return (start_string + ''.join(text_generated))

def get_name(cht: tio.Chatter):
    return cht.name

def pre_bot_run():
    model = tf.keras.models.load_model("NeuralPOAL/NLP_20K_CHAT/saved_model.h5", compile=False)
    vocab = json.load(open("NeuralPOAL/NLP_20K_CHAT/vocab.json", 'r'))
    return model, vocab

class Bot(commands.Bot):
    def __init__(self, model, vocab):
        super().__init__(token=bot_config.TWITCH_TOKEN, prefix="JABA", initial_channels=['pwgood', 'poal48'])
        self.model = model
        self.vocab = vocab
        self.banned = json.load(open("banned.json", 'r'))

    async def event_ready(self):
        await self.get_channel("poal48").send(f"COPIUM JABA is now running | pomidor version | model loaded")
    
    async def event_message(self, message):
        if message.echo: return
        if not message.author.name in self.banned:
            await self.handle_commands(message=message)
    
    @commands.command(name="ping")
    async def command_ping(self, ctx: commands.Context):
        await ctx.reply(f"COPIUM JABA is running | pomidor verison | model loaded")

    @commands.command(name="wires")
    @commands.cooldown(rate=1, per=15, bucket=commands.Bucket.default)
    async def command_wires(self, ctx: commands.Context):
        ctx.message.content = " ".join(ctx.message.content.split()[2:])
        if len(ctx.message.content) > 100:
            await ctx.reply("Too many words JABA TeaTime")
            return
        text = generate_text(self.model, ctx.message.content+u" ", 0.9876, 150, self.vocab).split()
        for tos_word in bot_config.TOS_WORDS:
            if tos_word in ''.join(text):
                await ctx.send("Жабья тос защита сработала JABA TeaTime")
                return
        if text[0][0] == "$" or text[0][0] == "!" or text[0][0] == "=" or text[0][0] == "*": text.insert(0, "( JABA )")
        for i in range(len(text)):
            if text[i][0] == "@": text[i] = "( JABA )"
            if text[i].lower().replace(',', '') in map(get_name, ctx.chatters): text[i] = "( JABA )"
            if text[i].lower() == "vanishme": text[i] = "( JABA )"
            if "https:" in text[i] or "http:" in text[i] or ".com" in text[i] or ".net" in text[i] or ".ru" in text[i] or \
                ".org" in text[i] or "gachi.gay" in text[i] or "kappa.lol" in text[i]: text[i] = "( JABA )"
        await ctx.reply(" ".join(text))


    @commands.command(name="ban")
    async def command_ban(self, ctx: commands.Context):
        if ctx.author.name in bot_config.moded:
            self.banned.append(ctx.message.content.split()[2].lower())
            json.dump(self.banned, open("banned.json", 'w'))
            await ctx.reply("banned JABA TeaTime")

    @commands.command(name="vanish")
    async def command_vanish(self, ctx: commands.Context):
        if ctx.author.name in bot_config.moded:
            await ctx.send("VanishMe JABA TeaTime")

model, vocab = pre_bot_run()
bot = Bot(model, vocab)
bot.run()