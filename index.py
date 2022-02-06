import discord
import os
import random
#import soberdate

busters = [
    "going for a walk",
    "drinking a cold glass of water",
    "taking ten deep breathes", 
    "calling somebody", 
    "twenty jumping jacks", 
    "doing some stretches", 
    "listening to your favourite song", 
    "a three minute meditation", 
    "slowly counting to ten",
    "closing your eyes for twenty seconds", 
    "imagining a beautiful landscape", 
    "telling yourself a joke", 
    "thinking of someone you love (furry friends included!)",
    "taking a nap", 
    "eating a healthy snack", 
    "reading a couple pages of a book", 
    "setting a goal for tomorrow",
    "jogging in place", 
    "writing in a journal", 
    "singing or humming your favourite song", 
    "listening to your favourite artist", 
    "doodling on scrap paper", 
    "drawing or colouring", 
    "cleaning one spot in your room", 
    "hand drumming on your table", 
    "finding a new use for something in your room", 
    "dancing (bonus points for dancing terribly)", 
    "writing somebody a letter, whether or not you want to send it", 
    "looking through old photos", 
    "making a gratitude list", 
    "listing your three greatest strengths", 
    "doing something kind for another", 
    "hugging somebody, if nobody is around then hugging yourself", 
    "solving a puzzle", 
    "ripping paper into tiny pieces", 
    "whistling or playing an instrument", 
    "watching a good movie", 
    "watching kitten videos on YouTube", 
    "taking some nice pictures (inside or outside)", 
    "writing an intensive list of anything you can think of", 
    "making a really goofy smile and seeing how long you can hold it",
    "writing a thank you note to yourself", 
    "chewing gum", 
    "drawing your own comic", 
    "reading a magazine or a blog",
    "seeing how high you can count to", 
    "twiddling your thumbs as fast as you can", 
    "making a vision board", 
    "giving yourself a genuine compliment", 
    "laughing as loudly as you can", 
    "smiling in the mirror", 
    "notice five things you can see without moving your vision", 
    "downloading a new game", 
    "planning a fun trip you may go on someday", 
    "mentally noting the emotions you're feeling at the moment", 
    "making a tower out of a deck of cards", 
    "listening to nature sounds, either outside or online", 
    "tensing every muscle as much as you can for five seconds, then releasing"
]

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    #img = discord.File("tenor.png")
    if message.author == client.user:
        return
    returnMessage = ''
    if message.content == '$craving':
        returnMessage = cravingBuster(message)
    if message.content == '$cat':
        returnMessage = catPic(message)
    await message.channel.send(returnMessage)
        
def cravingBuster(message):
    return f"Stay strongly {message.author.name}! Maybe try {random.choice(busters)}?"

def catPic(message):
    #headers_dict = {"x-api-key": "cookie1=value1"}
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    return response.url

client.run(os.getenv('TOKEN'))
