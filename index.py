import discord
import os
import random
import requests
import random
import json
from bs4 import BeautifulSoup
#from pprint import pprint

import cravingkickers
from discord.ext import commands
from html2markdown import html2markdown

bot = commands.Bot(command_prefix='$')

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
    if message.content == '$video':
        returnMessage = recoveryVideo()
    if message.content == '$dr' or message.content == '$dailyreflections':
            returnMessage = dailyReflection()
    if returnMessage != ' ':
        await message.channel.send(returnMessage)
        
def cravingBuster(message):
    return f"Stay strongly {message.author.name}! Maybe try {random.choice(cravingkickers.kickers)}?"

def catPic():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    return "AWWWW! Look at this cat!\n" + response.json()[0]['url']

def justForToday():
    req = requests.get('https://www.jftna.org/jft/')
    text = []
    soup = BeautifulSoup(req.text, 'html.parser')
    for br in soup.find_all("br"):
        br.replace_with("\n" + br.text)
    body = soup.find_all('tr')
    for row in body:
        rowText = row.get_text().strip()
        text.append(rowText)
    pprint(text)
    jft = f"\n__**{text[1]}**__\n{text[0]}\n\n*{text[3]}\n{text[4]}*\n\n{text[5]}\n\n*{text[6]}*"
    return jft

def dailyReflection():
    """Gets todays daily reflection from https://www.aa.org/daily-reflections"""
    req = requests.get('https://www.aa.org/daily-reflections')
    text = []
    soup = BeautifulSoup(req.text, 'html.parser')
    reflection = soup.find_all("div", {"class": "reflection"})
    markdown = html2markdown(str(reflection))
    return  markdown

def recoveryVideo():
    """Gets a random youtube url from the text file in the assets directory"""
    with open("assets/Recovery_Vids.txt", "r") as f:
        url_list = f.read().splitlines()
        url = random.choice(url_list)
    return "Enjoy this recovery video!\n" + url
         

client.run(os.getenv('TOKEN'))
