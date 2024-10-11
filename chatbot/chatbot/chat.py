import random
import json
import torch
import requests
import spacy
from coronachatbot import coronachatbot
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load intents.json with UTF-8 encoding
file_path = 'intents.json'
try:
    with open(file_path, 'r', encoding='utf-8') as json_data:
        intents = json.load(json_data)
    print("File loaded successfully.")
except Exception as e:
    print(f"Error loading file: {e}")
    raise

# Load trained model data
FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

# Initialize model
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "BOT"

def local_get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])

    return "I do not understand..."

nlp = spacy.load("en_core_web_md")

api_key = "648d829da30c83491b16a67402c54fc4"

def get_weather(city_name):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(api_url)
    response_dict = response.json()
    
    if response.status_code == 200:
        weather = response_dict["weather"][0]["description"]
        degKTemp = response_dict["main"]["temp"]
        degCTemp = round(degKTemp - 273.15, 1)
        prediction = f"In {city_name}, the current weather is: {weather}. The current Temperature is {degCTemp}°C."
        return prediction
    else:
        print(f'[!] HTTP {response.status_code} calling [{api_url}]')
        return None

def get_covid_stats(statement):
    covid_country = nlp("Covid stats in a country")
    covid_statement = nlp(statement)
    min_similarity = 0.7
    simil = covid_country.similarity(covid_statement)
    print(f"similarity {simil}")
    
    if simil >= min_similarity:
        for ent in covid_statement.ents:
            if ent.label_ == "GPE":  # GeoPolitical Entity
                country = ent.text
                break
        else:
            return None
    else:
        return None

    req_url = f'https://covid-19.dataflowkit.com/v1/{country}'
    response = requests.get(req_url)
    response_dict = response.json()

    if "Last Update" in response_dict:
        return (f"Last Updated: {response_dict['Last Update']}\n"
                f"Total Cases: {response_dict['Total Cases_text']}\n"
                f"Total Deaths: {response_dict['Total Deaths_text']}\n"
                f"Total Recovered: {response_dict['Total Recovered_text']}")
    else:
        return "Could not retrieve COVID-19 stats."

def chatbot(statement):
    raw_statement = statement
    weather = nlp("Current weather in a city")
    statement = nlp(statement)
    min_similarity = 0.75
    simil = weather.similarity(statement)
    print(f"similarity {simil}")

    if simil >= min_similarity:
        for ent in statement.ents:
            if ent.label_ == "GPE":  # GeoPolitical Entity
                city = ent.text
                break
        else:
            return "You need to tell me a city to check."

        city_weather = get_weather(city)
        if city_weather is not None:
            return city_weather
        else:
            covid_resp = get_covid_stats(raw_statement)
            if covid_resp is not None:
                return covid_resp
            else:
                return local_get_response(raw_statement)
    else:
        covid_resp = get_covid_stats(raw_statement)
        if covid_resp is not None:
            return covid_resp
        else:
            return local_get_response(raw_statement)

def get_response(msg):
    return chatbot(msg)
