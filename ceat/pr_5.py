import nltk
from nltk.chat import Chat

pairs = [
    [
        r"Hi|Hello|Hey",
        ["Hello How may i assist you?"]
    ],
    [
        r"What is your Name?",
        ["Myself PyBot! A chatbot developed using python."]
    ],
    [
        r"What is 2+2?",
        ["Answer is: 4"]
    ],
    [
        r"What is two plus two?",
        ["Answer is: 4"]
    ],
    [
        r"quit",
        ["Thank you for using my services!!"]
    ],
]

print("Welcome to PyBot!!")
chat = Chat(pairs)
chat.converse()