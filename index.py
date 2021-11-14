import discord
import os
import random

busters = [
    "going for a walk",
    "drinking a cold glass of water",
    "taking ten deep breathes"
]

img = discord.File("tenor.png")
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$':
        await message.channel.send(f"Stay strong {message.author.name}! Maybe try {random.choice(busters)}?", file=img)

client.run(os.getenv('TOKEN'))
