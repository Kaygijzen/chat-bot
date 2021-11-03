from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import random

# TODO: expand the chatbot

app = Flask(__name__)

english_bot = ChatBot(
    "Chatterbot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri='sqlite:///database.sqlite3'
)
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.mycorpus")
trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html", id=random.randint(1, 1000))


@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
