import time
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route('/helloWorld')
def hellovey():
    return "Hello From Aidana!"

@app.route('/healthz')
def healthz():
    return "OK"

@app.route('/healthx')
def healthx():
    time.sleep(3);
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
