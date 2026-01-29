#import project files
import faker
import league
import api
import discord


#
#
#intents = discord.Intents.all()
#intents.members = True
#intents.message_content = True
#membercacheflags=discord.MemberCacheFlags.from_intents(intents)

discord_client = faker.DiscordClient()
league_trackers = {}

@discord_client.event
async def get_user(riot_id):
    league_trackers[riot_id] = league.LeagueThing(riot_id)
    print(league_trackers)


discord_client.run(api.discord_token)