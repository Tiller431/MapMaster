from bottle import route, run
import conf
from api import beatmap



@route('/d/<mapID>')
def download(mapID):
    return "(WIP)"

@route('/s/<setID>')
def setInfo(setID):
    return setID

@route('/b/<mapID>')
def beatmapInfo(mapID):
    return beatmap.getBeatmap(mapID)

run(host='0.0.0.0', port=8080)