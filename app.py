from flask import Flask, render_template, request
import random
from bot import Bot

# TODO: expand the chatbot

app: Flask = Flask(__name__)
bot: Bot = Bot()


@app.route("/")
def home():
    return render_template("index.html", id=random.randint(1, 1000))


@app.route("/get_response")
def get_response():
    text = request.args.get("msg")
    return str(bot.get_response(text))


if __name__ == "__main__":
    app.run()
