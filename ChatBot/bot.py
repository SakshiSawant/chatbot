from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
chat_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(chat_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("data/data.yml")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg") #get data from input,we write js to index.html
    return str(chat_bot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True)
