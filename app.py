import threading
import time
import urllib3

def runfor():
    http = urllib3.PoolManager()
    while True:
        resp = http.request('GET', 'https://rsahdaweb.azurewebsites.net/projects')
        print(resp.status)
        time.sleep(900)

x = threading.Thread(target=runfor)
x.start()

from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("https://rsahdaweb.azurewebsites.net/", code=302)

app.run(host='0.0.0.0', port=81)