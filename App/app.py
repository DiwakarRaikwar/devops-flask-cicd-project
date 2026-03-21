from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello Diwakar!<br>IP: {socket.gethostbyname(socket.gethostname())}<br>Time: {datetime.datetime.now()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)