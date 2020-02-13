import discord
from discord.ext import commands

class Tarkov(commands.Cog):
    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()
    async def _on_ready(self):
        await client.change_presence(status=discord.Status.idle, activity=discord.Game('Roubles rule!') )
        print("Bot is ready!")
