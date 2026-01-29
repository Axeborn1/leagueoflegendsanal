#program imports
import api



#Other module import
import discord
import os
import asyncio

#creates DiscordClient as a child of the client class from discord. This class will manage the discord side of the project.
class DiscordClient(discord.Client):
    def __init__(self):
        #edits the discord client init function to automatically use all intents and cahce flags
        intents = discord.Intents.all()
        intents.members = True
        intents.message_content = True
        membercacheflags=discord.MemberCacheFlags.from_intents(intents)

        #collects the normal discord client init function to make sure the client works correctly
        super().__init__(intents=intents,member_cache_flags=membercacheflags) 

    #edits the on message event function to make the client automatically respond.
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('Faker!'):
            await message.channel.send(message.content[7:10])
            print(message.content[7:10])
            if message.content[7:10]=="add":
                await message.channel.send("BAZINGA")
                await self.get_user(message.content[11:])
    
    async def get_user(self,riot_id):

        return riot_id









