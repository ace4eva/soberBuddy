import discord
import os
import random

busters = [
    "going for a walk",
    "drinking a cold glass of water",
    "taking ten deep breathes"
]

img = discord.Embed({url="https://i.pinimg.com/originals/3a/9f/32/3a9f32461468488a6758c317859ab4ad.gif"}) )

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$':
        await message.channel.send(f"Stay strong {message.author.name}! Maybe try {random.choice(busters)}?", embed=img)

client.run(os.getenv('TOKEN'))
