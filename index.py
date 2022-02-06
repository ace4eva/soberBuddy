import discord
import os
import random
import requests
import json

import cravingkickers

#import soberdate

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    #img = discord.File("tenor.png")
    
    #if message.content.startsWith() != "$":
    #    return
    if message.author == client.user:
        return
    returnMessage = ' '
    if message.content == '$craving':
        returnMessage = cravingBuster(message)
    if message.content == '$cat':
        returnMessage = catPic(message)
    if returnMessage != ' ':
        await message.channel.send(returnMessage)
        
def cravingBuster(message):
    return f"Stay strongly {message.author.name}! Maybe try {random.choice(kickers)}?"

def catPic(message):
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    return response.json()[0]['url']

client.run(os.getenv('TOKEN'))
