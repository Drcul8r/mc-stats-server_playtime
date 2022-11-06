import json
import os.path

total_playtime = 0
season_old = 1
player_uuid = 0

#Function
def season_old(total_playtime,season_old,player_uuid):
      if os.path.isfile("stats"+season_old+"/"+player_uuid+".json"):
            x = open("stats"+season_old+"/"+player_uuid+".json", encoding='utf-8')
            y = json.load(x)
            print("season_old "+season_old+":", (y['stats']['minecraft:custom']['minecraft:play_one_minute'])/72000)
            total_playtime = (y['stats']['minecraft:custom']['minecraft:play_one_minute'])
      else:
            return ("season_old "+season_old+": No data achieved.")

# main
player_uuid = input("What is the UUID of your player?\n>")
season_old(total_playtime,season_old,player_uuid)
