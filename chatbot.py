
from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you. You can call me ChatBot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"I am fine",
        ["Great to hear that!", "How can I help you?",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "It was nice talking to you. Goodbye!"]
    ],
]
chatbot = Chat(pairs, reflections)
print("Hello! I am your chatbot. How can I help you today?")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Bot: Bye! Take care.")
        break
    bot_response = chatbot.respond(user_input)
    print(f"Bot: {bot_response}")