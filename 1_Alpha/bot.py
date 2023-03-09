import nextcord
import logging
import random
from datacon import data
import asyncio
import time
import signal


token = "MTA1OTM0ODExNjQ5MjUyNTU5OQ.GgEoSv.2I3xEYHD6m61X1KV-rAxaBPl-oHqW1wdYc9h6s"

intents = nextcord.Intents.all()
intents.members = True

bot = nextcord.Client(intents=intents)

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

    default = True
    use_again = True

    if "idiot" in message.content:
        await message.channel.send("LOLOLOL Idiot")
    elif "shut" in message.content:
        await message.channel.send("No YOU shut up")
        time.sleep(4)
        await message.channel.send("Beech")
        return

    

    if default == True:
        if message.content.startswith("$debug"):
            use_again = False
            await message.channel.send("`Debug: Command Used`")

            if use_again == False:
                    await message.channel.send("`Please wait for 10 seconds to use that command again`")
                    return
    

    order_1 = True

    if order_1 == True:
        if message.content.startswith("i order you to mention SUS ZenZen"):
            await message.channel.send("Yes Boss")
            time.sleep(2)
            await message.channel.send(f"{message.author.mention(808965166926135307)}")


    if message.content.startswith("stop mention now"):
        order_1 = False
        return

    

        




bot.run(token)