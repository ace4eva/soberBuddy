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
    #req = urllib.request.urlopen('https://www.jftna.org/jft/')
    #req = requests.get('https://www.jftna.org/jft/')
    #root = etree.fromstring("https://www.jftna.org/jft/")
    #body = etree.tostring(root.getroot()) 
    #print(body)
    #for row in x.iter('tr'):
     #   print(etree.parse(row.text))
      #  print("\n----")
    req = requests.get('https://www.jftna.org/jft/')
    body = BeautifulSoup(req.text, 'html.parser')
    #[text for text in body.stripped_strings]
    #pprint(text)
    test = body.find_all('tr')
    for row in test:
        pprint(row.get_text().strip())
    r = requests.get('https://www.jftna.org/jft/')
    text = r.text
    table = etree.HTML(text).find("body/table")
    rows = iter(table)
    jft = []
    for row in rows:
        values = [col.text for col in row]
        jft.append(values)
    return f"\n{jft[1][0]}\n{jft[3][0]}\n{jft[4][0]}\n"
         

client.run(os.getenv('TOKEN'))
