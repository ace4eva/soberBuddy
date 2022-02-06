import discord
import os
import random
import requests
import json
from lxml import etree

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
    if message.content == '$jft':
        jft = getJustForToday()
        printJustForToday(jft)
    if returnMessage != ' ':
        await message.channel.send(returnMessage)
        
def cravingBuster(message):
    return f"Stay strongly {message.author.name}! Maybe try {random.choice(cravingkickers.kickers)}?"

def catPic(message):
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    return response.json()[0]['url']

def getJustForToday():
    r = requests.get('https://www.jftna.org/jft/')
    text = r.text
    table = etree.HTML(text).find("body/table")
    rows = iter(table)
    headers = [col.text for col in next(rows)]
    jft = []
    for row in rows:
        values = [col.text for col in row]
        jft.append(values)
        #print(dict(zip(headers, values)))
    return jft

def printJustForToday(jft):
    print("TODO GET DATE IM TOO LAZY TO DO NOW")
    print(jft[1][0])
    print()
    print(jft[3][0])
    print()
    print(jft[4][0])
         

client.run(os.getenv('TOKEN'))
