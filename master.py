from bottle import route, run

@route('/')
def index():
    return "OK"

run(host='localhost', port=8080)