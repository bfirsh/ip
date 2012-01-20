from flask import Flask, jsonify, request
import socket

socket.setdefaulttimeout(5)

app = Flask(__name__)

@app.route('/')
def index():
    d = {
        'ipv6': None,
        'hostv6': None,
        'ipv4': None,
        'hostv4': None,
    }
    d['ipv4'] = request.remote_addr.rsplit(':', 1)[-1]
    try:
        d['hostv4'] = socket.gethostbyaddr(d['ipv4'])[0]
    except: # oh so many things can go wrong
        pass
    if ':' in request.remote_addr:
        d['ipv6'] = request.remote_addr
        try:
            d['hostv6'] = socket.gethostbyaddr(d['ipv6'])[0],
        except:
            pass
    res = jsonify(**d)
    if request.args.get('callback', ''):
        res.data = '%s(%s)' % (request.args['callback'], res.data)
    return res

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


