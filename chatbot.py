from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import random


bot = ChatBot('MyBot')


trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")


jokes = [

"Why do programmers hate nature? Because it has too many bugs! 😂",

"Why was the computer cold? It forgot to close its Windows! 😂",

"Why do Java developers wear glasses? Because they don't C#! 😂",

"What do you call 8 hobbits? A hobbyte! 😂",

"Why did the Python developer go broke? Because he couldn't cache his money! 😂"

]


def get_bot_response(message):


    msg = message.lower()


    greetings = ['hi','hello','hey']

    if msg in greetings:
        return random.choice([

            "Hello! 😊",

            "Hi there! 👋",

            "Hey! How are you?",

            "Hello! Nice to meet you."

        ])



    elif "how are you" in msg:
        return "I am doing well. How about you? 😊"



    elif "i am good" in msg:
        return "That's great to hear! 😄"



    elif "what about you" in msg:
        return "I am always happy to chat with you! 🤖"



    elif "joke" in msg:
        return random.choice(jokes)



    elif "lunch" in msg:
        return "I don't eat food, but I hope you had a tasty lunch! 🍔"



    elif "dinner" in msg:
        return "I don't eat dinner, but thanks for asking! 🍕"



    elif "breakfast" in msg:
        return "No breakfast for me. I run on Python code! 🐍"



    elif "your name" in msg:
        return "My name is MyBot. 🤖"



    elif "who made you" in msg:
        return "Likki developed me using Flask and ChatterBot. 🚀"



    elif "python" in msg:
        return "Python is a powerful programming language used in AI, web development, automation and more."



    elif "ai" in msg:
        return "AI stands for Artificial Intelligence. It enables machines to mimic human intelligence."



    elif "thank" in msg:
        return "You're welcome! 😊"



    elif "bye" in msg:
        return "Goodbye! Have a wonderful day! 👋"



    else:

        response = bot.get_response(message)

        return str(response)