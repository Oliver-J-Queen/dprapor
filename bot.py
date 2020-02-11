import discord


from discord.ext import commands

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

client.run('Njc2ODgwMDM5ODQ1MDM2MDk4.XkMHsw.Td-gHZ09KUCLq7XGakdD3gYG8-k')
