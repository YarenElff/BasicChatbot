from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("chatbot", read_only=False, 
              logic_adapters=[
                  {
                  "import_path" : "chatterbot.logic.BestMatch",
                  "default_response" : "Sorry , I don't have an answer.",
                  "maximum_similarity_treshold" : 0.9             
                  }
                  ])

list_to_train = [
                "Hi!",
                "Hi there!",
                "What's your name?",
                "I am a chatbot.",
                "How old are you?",
                "I am ageless.",
                "Do you have IPhone ?"
                "I have everything.",
                "Who am i?",
                "You are a human.",
                "What is your job ?",
                "I'm here to answer your questions.",
                "I don't know what you're talking about."
]

list_trainer = ListTrainer(bot)

list_trainer.train(list_to_train)

while True:
    user_response = input("User : ")
    print("ChatBot :", str(bot.get_response(user_response)))