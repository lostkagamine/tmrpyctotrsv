# VALUE TO RETURN: The number '4' in any format
# TRIGGER: The string 'pls four' in any discord channel the bot is in
# AUTHOR: ry00001 (ry00001#3487)
# DEPENDENCIES: discord.py rewrite

import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix='pls ')

with open('./config.json') as f:
    config = json.load(f)

@bot.command()
async def four(ctx):
    await ctx.send(str(3+1))

@bot.event
async def on_ready():
    print('four lol dude, four (CONNECTED)')
    bot.remove_command('help')
    await bot.change_presence(game=discord.Game(name='with the number 4', type=0))

bot.run(config.get('token'))