import discord
import os
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


client = commands.Bot(command_prefix = "-")
#extension / cog load
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
#testing area
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

@client.event
async def on_member_remove(member):
    print(f'{member} left the server.')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit = amount)

@client.command()
async def test(ctx, arg):
    await ctx.send(arg)

@client.command()
async def ping(ctx):
    await ctx.send(f'Latency: {round(client.latency * 1000)}ms')
#checking

client.run('yeet')
