from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import json


class Bot:
    """Chatbot Py class"""

    def __init__(self):
        """init bot and train"""
        self.bot = ChatBot(
            "Chatterbot",
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///database.sqlite3'
        )

        trainer = ChatterBotCorpusTrainer(self.bot)
        trainer.train(
            "./data/mycorpus",
            "chatterbot.corpus.english"
        )

        """train based on extracted corpus"""
        listtrainer = ListTrainer(self.bot)
        # Use file to refer to the file object
        with open("./data/my_conversations.json") as file:
            data = json.load(file)
            listtrainer.train(data)

    def get_response(self, text):
        return str(self.bot.get_response(text))
