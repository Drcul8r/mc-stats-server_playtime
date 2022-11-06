import json
import os.path

player_uuid = ['2880cdb4-d96f-4287-a787-decade62c6d8','76960189-329e-48ae-bced-1e1404bc119b','b3f73b20-b763-4562-895d-fd4cc3ea795b','83dd1899-37fe-4fad-8efe-14d47874cbc0','11121555-07d4-4514-954d-ab7e9f20f0ba','fd8b1e71-f888-4ad4-b70b-a1f97fbdaabc','8ffc9dc8-3e98-47ec-a9ae-c9c479daf7dd','59ad74b2-9862-4d43-9bad-79a7307ff612','381f7f88-b4d6-4a87-9b21-5071d7be32a6','4612ccbe-7014-4c00-ad2f-e175f12f26d6','9613c6fd-c019-4f76-9658-b26dd8538fc7','af7c0170-cba4-4e83-9417-aeee23c3ad82','c45dde35-562f-4007-ac20-d83a8415c59f','d18da12c-1047-46df-8da8-6a1bcf5d5ca0','ea038e71-96c0-4264-b737-32280b636583','ed72a6be-27d7-45bf-98f0-fcf2945d9d39','f1d161cb-c837-4bd9-a52d-aeaefd49c9a8','5a71a113-c10f-4d4a-a3f5-3db2850abb55','23a5a205-0556-41e8-b55c-a78b11569921','1b6ec58d-a1b0-4bef-957e-5c1428d13a3c','96633b15-abe0-46bf-946f-d34aff30d4a7','747432c7-6177-4202-8c74-339892963a2f','a338a71d-5dec-4819-999d-3c0c3b6cabd7','ac5c9600-4c55-4f6a-81a5-1ba499085a33','5748e56a-bbba-4441-9dac-7c7c33c02654','d647e227-1f19-47ea-85c8-12c8fe0b588a','29981af1-4e77-4ce6-81cf-a3d278cf5963','b906ba06-98fb-4660-a1e6-767976a8b517','0074b5b8-2c38-4282-9526-487690f7072b','53ff2b35-9c2a-43a2-a26c-4bfcfa53c5e2']

#Function
def individual(player_uuid):
      player_uuid_1 = ''
      w = 0
      total_playtime = 0
      for w in range(0,30):
            def season_old(z,player_uuid_1):
                  path = "stats"+str(z)+"/"+player_uuid_1+".json"
                  if z != 3:
                        if os.path.isfile(path):
                              x = open(path, encoding='utf-8')
                              y = json.load(x)
                              season_time = ((y['stats']['minecraft:custom']['minecraft:play_one_minute'])/72000)
                              print("Season",z,":",season_time)
                              return float(season_time)
                        else:
                              return 0
                  else:
                        print("Season 3 : 0")
                        return 0

            def season_new(z,player_uuid_1):
                  path = "stats"+str(z)+"/"+player_uuid_1+".json"
                  if z != 3:
                        if os.path.isfile(path):
                              x = open(path, encoding='utf-8')
                              y = json.load(x)
                              season_time = ((y['stats']['minecraft:custom']['minecraft:play_time'])/72000)
                              print("Season",z,":",season_time)
                              return float(season_time)
                        else:
                              return 0
                  else:
                        print("Season 3 : 0")
                        return 0

            # main
            player_uuid_1 = player_uuid[w]
            print("")
            for z in range(1,9):
                  total_playtime += season_old(z,player_uuid_1)
            for z in range(9,12):
                  total_playtime += season_new(z,player_uuid_1)
            print("\n",player_uuid_1,"total playtime is:",total_playtime,"\n")
print("Player: _0liver | UUID: 53ff2b35-9c2a-43a2-a26c-4bfcfa53c5e2\nPlayer: EPICGamer123454 | UUID: 0074b5b8-2c38-4282-9526-487690f7072b\nPlayer: drcul8r | UUID: 2880cdb4-d96f-4287-a787-decade62c6d8\nPlayer: Zaphod987 | UUID: 76960189-329e-48ae-bced-1e1404bc119b\nPlayer: Temet0 | UUID: b3f73b20-b763-4562-895d-fd4cc3ea795b\nPlayer: _YeetMan420_ | UUID: 83dd1899-37fe-4fad-8efe-14d47874cbc0\nPlayer: Peepo_2 | UUID: 11121555-07d4-4514-954d-ab7e9f20f0ba\nPlayer: bgbest123 | UUID: fd8b1e71-f888-4ad4-b70b-a1f97fbdaabc\nPlayer: Sabercrafter | UUID: 8ffc9dc8-3e98-47ec-a9ae-c9c479daf7dd\nPlayer: PickleJarMan206 | UUID: 59ad74b2-9862-4d43-9bad-79a7307ff612\nPlayer: PandaManSeven | UUID: 381f7f88-b4d6-4a87-9b21-5071d7be32a6\nPlayer: Maytea1 | UUID: 4612ccbe-7014-4c00-ad2f-e175f12f26d6\nPlayer: mappiboi | UUID: 9613c6fd-c019-4f76-9658-b26dd8538fc7\nPlayer: Bananaboi8801 | UUID: af7c0170-cba4-4e83-9417-aeee23c3ad82\nPlayer: P0intless1 | UUID: c45dde35-562f-4007-ac20-d83a8415c59f\nPlayer: Qwoski | UUID: d18da12c-1047-46df-8da8-6a1bcf5d5ca0\nPlayer: RiseAndEyes | UUID: ea038e71-96c0-4264-b737-32280b636583\nPlayer: Likeacreaper457 | UUID: ed72a6be-27d7-45bf-98f0-fcf2945d9d39\nPlayer: Ed_KooZ | UUID: f1d161cb-c837-4bd9-a52d-aeaefd49c9a8\nPlayer: SniperMyersJr | UUID: 5a71a113-c10f-4d4a-a3f5-3db2850abb55\nPlayer: P0PP7 | UUID: 23a5a205-0556-41e8-b55c-a78b11569921\nPlayer: Spurstimelord | UUID: 1b6ec58d-a1b0-4bef-957e-5c1428d13a3c\nPlayer: Lazangies | UUID: 96633b15-abe0-46bf-946f-d34aff30d4a7\nPlayer: Matt2only | UUID: 747432c7-6177-4202-8c74-339892963a2f\nPlayer: MWiggy | UUID: a338a71d-5dec-4819-999d-3c0c3b6cabd7\nPlayer: jakeypopples | UUID: ac5c9600-4c55-4f6a-81a5-1ba499085a33\nPlayer: clytz | UUID: 5748e56a-bbba-4441-9dac-7c7c33c02654\nPlayer: ExtremeKitten457 | UUID: d647e227-1f19-47ea-85c8-12c8fe0b588a\nPlayer: Hollowed_Skele | UUID: 29981af1-4e77-4ce6-81cf-a3d278cf5963\nPlayer: ipcMF | UUID: b906ba06-98fb-4660-a1e6-767976a8b517\n")
individual(player_uuid)