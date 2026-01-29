#program imports
import api



#Other module import
import discord
import os
import random
import asyncio


class DiscordClient(discord.Client):   
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')

#define intents
#intents = discord.Intents.all()
#intents.members = True
#intents.message_content = True
#membercacheflags=discord.MemberCacheFlags.from_intents(intents)
#client = discord.Client(intents=intents,member_cache_flags=membercacheflags)
#
#primary_server = "The Testing Ground"
#
#
##on ready. 
#@client.event
#async def on_ready():
#    print(f'{client.user} has connected to Discord!')
#    guild = discord.utils.get(client.guilds, name=primary_server)
#    print(guild.name)
#    for member in guild.members:
#        print(member)
#
##when a message is sent
#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#    if message.content.startswith('!'):
#        message.content = message.content[2:]
#        await decide(message)
#
##asks the descision AI what to do
#async def decide(message):
#    decision = await dAI.make_descision(message.content)
#    if decision == "reply":
#        await reply(message)
#    elif decision == "ask":
#        await ask(message)
#    elif decision == "ignore":
#        await ignore(message)
#    elif decision == "fail":
#        print("Failed to make decision")
#        await ignore(message)
#
##analyses the messsage using the analysis AI and then generates a message using the message AI.
#async def reply(message):
#    message.content = f"This message was sent by {message.author}. They have said: \n" + message.content
#    analyze_reply = await aAI.analyze_reply([message.content,f"Server sent: {message.guild.name}",f"Channel name: {message.channel.name}","Descision: reply"])
#    reply = await mAI.reply(analyze_reply)
#    await message.channel.send(reply)
#
#async def ask(message):
#    pass
#
#async def ignore(message):
#    pass




