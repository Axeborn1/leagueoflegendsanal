#import project files
import faker
import league
import api
import discord




intents = discord.Intents.all()
intents.members = True
intents.message_content = True
membercacheflags=discord.MemberCacheFlags.from_intents(intents)

discord_client = faker.DiscordClient(intents=intents,member_cache_flags=membercacheflags)

discord_client.run(api.discord_token)