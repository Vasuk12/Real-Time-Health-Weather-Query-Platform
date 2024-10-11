import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# Load the spaCy model globally before chatterbot tries to use it
spacy_model = spacy.load("en_core_web_sm")

# Initialize the chatbot
coronachatbot = ChatBot(
    'CoronaBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training With Own Questions 
trainer = ListTrainer(coronachatbot)

training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()
training_data_personal = open('training_data/personal_ques.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer.train(training_data)

# Training With Corpus
trainer_corpus = ChatterBotCorpusTrainer(coronachatbot)

trainer_corpus.train(
    'chatterbot.corpus.english'
)
