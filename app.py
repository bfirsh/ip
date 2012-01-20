from flask import Flask, jsonify, request
import socket

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.remote_addr
    ipv4 = request.remote_addr.rsplit(':', 1)[-1]
    return jsonify(
        ip=ip,
        ipv4=ipv4,
        host=socket.gethostbyaddr(ipv4)[0]
    )

if __name__ == '__main__':
    app.run(debug=True)


