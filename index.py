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
        returnMessage = catPic()
    if message.content == '$jft':
       returnMessage = justForToday()
    if returnMessage != ' ':
        await message.channel.send(returnMessage)
        
def cravingBuster(message):
    return f"Stay strongly {message.author.name}! Maybe try {random.choice(cravingkickers.kickers)}?"

def catPic():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    return response.json()[0]['url']

def justForToday():
    r = requests.get('https://www.jftna.org/jft/')
    text = r.text
    x = etree.parse('https://www.jftna.org/jft/')
    for row in x.iter('tr'):
        print(etree.parse(row.text))
        print("\n----")
    table = etree.HTML(text).find("body/table")
    rows = iter(table)
    jft = []
    for row in rows:
        values = [col.text for col in row]
        jft.append(values)
    return f"\n{jft[0][0]}\n{jft[3][0]}\n{jft[4][0]}\n"
         

client.run(os.getenv('TOKEN'))
