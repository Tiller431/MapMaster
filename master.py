from bottle import route, run
import conf



@route('/d/<mapID>')
def download(mapID):
    return conf.getConf("key")

@route('/s/<setID>')
def setInfo(setID):
    return setID

@route('/b/<mapID>')
def beatmapInfo(mapID):
    return mapID

run(host='localhost', port=8080)