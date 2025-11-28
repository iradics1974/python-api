from flask import Flask, jsonify
import socket
import platform

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello GitOps 2.0!", 200

@app.route("/info")
def info():
    return jsonify({
        "host": socket.gethostname(),
        "system": platform.system(),
        "release": platform.release(),
    })

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
