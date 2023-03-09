import nextcord
from nextcord.ext import commands
from nextcord import voice_client
import logging
import random
from datacon import data
import asyncio


token = "OTE2NTM1MzEzNjk2OTY4NzY0.GbtC4q.QOi02_ejwxmmSBGFYAqboUK4dodHtEY7Z0JF3o"

intents = nextcord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
        await bot.change_presence(activity=nextcord.Game(name='Test Developer\'s Application'))
        print('Agent {0.user}')

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')

    if message.content.startswith("$generate_pix"):
        await message.channel.send("link sent")
        await message.channel.send(random.choice(data))
        

    if message.content.startswith("$join"):
        if not message.author.voice:
            await message.channel.send("You are not in a voice channel")
        else:
            channel = message.author.voice.channel
            await channel.connect()



bot.run(token)