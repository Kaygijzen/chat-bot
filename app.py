from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import random

# TODO: expand the chatbot

# deze laat één chatbot tegen zichzelf praten

app = Flask(__name__)

default_bot = ChatBot(
    "Chatterbot1",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

trainer = ChatterBotCorpusTrainer(default_bot)
trainer.train(
    "./data/mycorpus",
    "chatterbot.corpus.english"
)


@app.route("/")
def home():
    return render_template("index.html", id=random.randint(1, 1000))


@app.route("/get_response")
def get_response():
    text = request.args.get("msg")
    return str(default_bot.get_response(text))


if __name__ == "__main__":
    app.run()
