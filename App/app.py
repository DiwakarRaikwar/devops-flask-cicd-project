from flask import Flask
import redis
import socket
import datetime

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379)

@app.route("/")
def home():
    count = r.incr('hits')
    return f"Hello Diwakar!<br>Visits: {count}<br>IP: {socket.gethostbyname(socket.gethostname())}<br>Time: {datetime.datetime.now()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)