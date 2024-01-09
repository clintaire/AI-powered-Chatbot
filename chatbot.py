from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# You can add more training data or customize responses as needed
# trainer.train([
#     'What is your name?',
#     'My name is Aire.',
#     'How are you?',
#     'I am doing well, thank you!'
# ])

# Get a response from the chatbot
response = chatbot.get_response('Hello, how are you?')
print(response)
