# Code modified from https://github.com/cree-py/birthdaybot

import discord
from discord.ext import commands
import json as jason
import datetime
import asyncio


@bot.command()
async def setSoberDate(ctx):
    '''Set a soberdate.'''
    member = ctx.message.author.id
    await ctx.send("What is your SoberDate? Please use MM/DD format.")
    def check(user):
        return user == ctx.message.author and user == ctx.message.channel
    msg = await bot.wait_for('message', check=check)
    try:
        list = msg.split("/")
        if list[0] > 13 or list[0] < 1:
            await ctx.send("Invalid date.")
            await ctx.send("Aborting...")
            return
        else:
            pass
            
        if list[0] in (1, 3, 5, 7, 8, 10, 12):
            if list[1] > 31 or list[1] < 1:
                await ctx.send("Invalid date.")
                await ctx.send("Aborting...")
                return
            else:
                pass
        elif list[0] in (4, 6, 9, 11):
            if list[1] > 30 or list[1] < 1:
                await ctx.send("Invalid date.")
                await ctx.send("Aborting...")
                return
            else:
                pass
        elif list[0] == 2:
            if list[1] > 29 or list[1] < 1:
                await ctx.send("Invalid date.")
                await ctx.send("Aborting...")
                return
            else:
                pass
        else:
            await ctx.send("Invalid date.")
            await ctx.send("Aborting...")
            return
    except:
        await ctx.send("Invalid date.")
        await ctx.send("Aborting...")
        return
    
    list = msg.split("/")
    month = list[0]
    day = list[1]
    
    
    
    with open('./dates.json', 'r+') as f:
        var = jason.load(f)
        var[member] = {'month': month, 'day': day}
        jason.dump(var, f, indent=4)
    