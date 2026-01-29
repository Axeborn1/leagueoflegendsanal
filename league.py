from riotwatcher import LolWatcher, RiotWatcher, ApiError
import api

lol_watcher = LolWatcher(api.riot_games)
riot_watcher = RiotWatcher(api.riot_games)

class LeagueThing():
    def __init__(self, riot_id):
        self.riot_id = riot_id
        self.riot_id = riot_id.split('#')
        print(self.riot_id)
        self.account = riot_watcher.account.by_riot_id('AMERICAS', self.riot_id[0], self.riot_id[1])


#my_region = 'na1'
#
#my_account = riot_watcher.account.by_riot_id('AMERICAS', 'Axeborn', '9253')
#
#me = lol_watcher.summoner.by_puuid(my_region, my_account['puuid'])
##print(me)
#
#my_ranked_stats = lol_watcher.league.by_puuid(my_region, me['puuid'])
##print(my_ranked_stats)
#
## First we get the latest version of the game from data dragon
#versions = lol_watcher.data_dragon.versions_for_region(my_region)
#champions_version = versions['n']['champion']
#
## Lets get some champions
#current_champ_list = lol_watcher.data_dragon.champions(champions_version)
#
##for champion in current_champ_list["data"].keys():
##    print(champion)
##print("BREAK")
##print()
#
#
#
#
#my_match_list = lol_watcher.match.matchlist_by_puuid(my_region,me['puuid'])
#
##print(my_match_list[0])
#last_match = lol_watcher.match.by_id(my_region, my_match_list[0])
#timeline = lol_watcher.match.timeline_by_match(my_region, my_match_list[0])
#
##for i in last_match["info"].keys():
##    print(i)
##
##print()
##print(last_match["info"]["participants"][0])
##
#
#
##for i in timeline["info"]:
##    print(i)
##print(timeline["info"]["frameInterval"])
##
##x=0
##for i in timeline["info"]["frames"]:
##    x+=1
##
##print(timeline["info"]["frames"][0].keys())
##print(x)
#
#