import nextcord
from nextcord.ext import commands
from nextcord import voice_client
import logging
import random
import nextwave
from datacon import data
import asyncio


token = "MTA1NzI3MDI0MjQ3ODM5OTQ4OA.GtSOZa.Ojl_ECm9ORrZh7u2uUa_B_GRJ06XpkyM0MdEic"

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