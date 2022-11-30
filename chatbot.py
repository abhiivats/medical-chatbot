# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend 🤗",
])
trainer.train([
    "PROBLEM",
    "SYMPTOMS?",
])
trainer.train([
    "HEADACHE",
    "CITRAZINE",
])
trainer.train([
    "COLD",
    "SINAREST TAB",
])
trainer.train([
    "FEVER",
    "PARACETAMOL",
])
trainer.train([
    "ALLERGY",
    "NEMUCELITE",
])
trainer.train([
    "VOMITTING",
    "YUNERAB-DSR",
])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(chatbot.get_response(query))