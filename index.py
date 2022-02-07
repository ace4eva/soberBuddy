import discord
import os
import random
import requests
import json
from lxml import etree
from bs4 import BeautifulSoup
from pprint import pprint

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
    req = requests.get('https://www.jftna.org/jft/')
    text = []
    bodybs = BeautifulSoup(req.text, 'html.parser')
    body = bodybs.find_all('tr')
    for row in body:
        rowText = row.i.get_text()
        #rowText = rowText.replace("<br>", "\n");
        text.append(rowText)
    pprint(text)
    jft = f"\n__**{text[1]}**__\n{text[0]}\n\n*{text[3]}*\n{text[4]}\n\n{text[5]}\n\n*{text[6]}*"
    return jft
         

client.run(os.getenv('TOKEN'))
