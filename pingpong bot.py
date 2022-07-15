

import time
import discord
from discord.ext import commands
intents = discord.Intents.default()

bot = commands.Bot(command_prefix= '$',intents=intents)




@bot.command()
async def ping(ctx, member : discord.Member):
    channel = member.voice.channel
    print()
    
    while  member.voice.self_mute == True:
        
        print("ping ponging")

        await member.move_to(bot.get_channel('channel id here'  ))
        
        time.sleep(1)
        
        await member.move_to(bot.get_channel('channel id here'  )))
    await member.move_to(channel)



@bot.command()
async def supercmd(ctx, member : discord.Member):
    i = 0
    
    while i != 200:
        i = i + 1
        await member.move_to(bot.get_channel('channel id here' )))       
        time.sleep(1)       
        await member.move_to(bot.get_channel('channel id here'  )))
        time.sleep(1) 
    


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')






bot.run('bot token here')