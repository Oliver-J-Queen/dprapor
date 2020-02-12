import discord
from discord.ext import commands
import logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = commands.Bot(command_prefix = "-")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

@client.event
async def on_member_remove(member):
    print(f'{member} left the server.')

@client.command
async def test(cntx):
    print(cntx)


client.run('Njc2ODgwMDM5ODQ1MDM2MDk4.XkRIyw.xrNN-tg2Z0aKcyTymRjWX8Ef_aE')
