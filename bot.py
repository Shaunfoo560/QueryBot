import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
import numpy as np
import pickle
import random
import json

lem = WordNetLemmatizer()
loaded_model = load_model('botModel')
bases = pickle.load(open('bases.pickle', 'rb'))

def bag_of_words(msg):
    msg_bases = [lem.lemmatize(word) for word in nltk.word_tokenize(msg)]
    bag = [0] * len(bases)

    for b in msg_bases:
        for i, base in enumerate(bases):
            if base == b:
                bag[i] = 1
                
    return np.array(bag)

tags = pickle.load(open('tags.pickle', 'rb'))
intents = json.loads(open('intents.json').read())

def get_response(msg):
    res = loaded_model.predict(np.array([bag_of_words(msg)]))[0]
    results = [[i, r] for i, r in enumerate(res) if r > 0.25]
    results.sort(key = lambda x: x[1], reverse = True)
    possible_intents = [{'intent': tags[r[0]], 'prob': str(r[1])} for r in results]

    for intent in intents['intents']:
        if intent['tag'] == possible_intents[0]['intent']:
            return random.choice(intent['responses'])