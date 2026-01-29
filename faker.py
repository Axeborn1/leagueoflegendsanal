#program imports
import api



#Other module import
import discord
import os
import asyncio


class DiscordClient(discord.Client):   
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('Faker!'):
            await message.channel.send('Hello World!')






