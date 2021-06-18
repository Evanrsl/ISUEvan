from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return " Congratulation, it's a web app!"

@app.route("/hi")
def who():
    return "Congratulations, this is another way to show HII!!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8088, debug = True)