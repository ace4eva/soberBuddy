import discord
import os
import random

busters = [
"Morgan is neat. ", 
"Morgan is great! ", 
"Morgan is good. "
] 

client = discord.Client()

@client.event

async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$'):
        await message.channel.send(random.choice(busters))

client.run(os.getenv('TOKEN'))
