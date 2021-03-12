import requests
import json
import conf

def getBeatmap(mapID):
    url = "https://osu.ppy.sh/api/get_beatmaps"
    apikey = conf.getConf("apikey")
    params = {
        "k": apikey,
        "b": int(mapID)
    }
    
    mapData = requests.get(url, params=params)
    return json.dumps(mapData.json())