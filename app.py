from flask import Flask, render_template, request
from chatbot import get_bot_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_response():
    msg = request.args.get('msg')
    return get_bot_response(msg)


if __name__ == "__main__":
    app.run(debug=True)