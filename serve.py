from flask import Flask, request
import json
import subprocess
import socket

app = Flask(__name__)

seed = 0

@app.route('/', methods = ['POST'])
def stress_cpu():
    global seed
    data = request.get_json()
    seed = data['num']
    subprocess.Popen(['python', 'stress_cpu.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return "Stressing CPU with seed {}".format(seed)

@app.route('/', methods = ['GET'])
def get_ip():
    private_ip = socket.gethostbyname(socket.gethostname())
    return "Private IP address: {}".format(private_ip)

if __name__ == '__main__':
    print(__name__)
    app.run(host="0.0.0.0", port=5000, debug=True)
