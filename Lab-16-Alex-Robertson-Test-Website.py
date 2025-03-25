from bottle import route, run, template
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!',
name=name)

run(host='192.168.1.11', port=8080, debug=True)