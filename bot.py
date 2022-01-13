from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


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

    def get_response(self, text):
        return str(self.bot.get_response(text))
