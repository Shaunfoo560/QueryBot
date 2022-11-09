import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.keras.models import Sequential
import numpy as np
import pickle
import random
import json

lem = WordNetLemmatizer()
collected_tags = sorted(set([]))
groupings = []
list_of_words = []

intents = json.loads(open('intents.json').read())
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # First, we tokenize the patterns in our intents.json and compile them in a list
        list_of_words.extend(nltk.word_tokenize(pattern))

        # Creating groupings for later usage when turning them into binary for the bag
        groupings.append(((nltk.word_tokenize(pattern)), intent["tag"]))

        # Saving tags for the bot to calculate probability for best responses
        if intent["tag"] not in collected_tags:
            collected_tags.append(intent['tag'])


# TConverting the tokenized patterns into their base forms (lemmatizing)
list_of_bases = sorted(set({lem.lemmatize(word) for word in list_of_words if word not in ['!', ',', ':', '?', '.']}))

# Saving tokenized and lemmatized patterns, as well as the tags
pickle.dump(list_of_bases, open('bases.pickle', 'wb'))
pickle.dump(collected_tags, open('tags.pickle', 'wb'))

# Generating output list of binary values initialized at 0 for all.
out_template = [0] * len(collected_tags)
xy_data = []

for group in groupings:
    bag = []

    # Converting tokenized words from patterns into their lowercase form and then lemmatizing them
    base_patterns = [lem.lemmatize(word.lower()) for word in group[0]]
    
    # Checking whether the word (base version) is present or not (1 indicates present, 0 means not present)
    for base in list_of_bases:
        if base in base_patterns:
           bag.append(1)
        else:
            bag.append(0)

    # Updating training list
    current_out = list(out_template)
    current_out[collected_tags.index(group[1])] = 1 
    xy_data.append([bag, current_out])

random.shuffle(xy_data)

# Splitting the training list
x_train = list((np.array(xy_data))[:, 0])
y_train = list((np.array(xy_data))[:, 1])


model = Sequential()
# initializing input layer shape as training input data size
model.add(Dense(256, activation = 'relu', input_shape = (len(x_train[0]),)))
model.add(Dropout(0.8))
model.add(Dense(128, activation = 'relu'))
model.add(Dropout(0.6))
model.add(Dense(64, activation = 'relu'))
model.add(Dropout(0.5))
# Final layer neurons matches number of tags, softmax to transform output into probabilities for our predictions
model.add(Dense(len(y_train[0]), activation = 'softmax'))

# Couldn't reach a clear conclusion on which optimizer to use even after tons of tests so i just commented out Adam
sgd = SGD(learning_rate = 0.01)
# adam = Adam(learning_rate = 0.01)

# Categorical crossentropy used due to multi-label/class classification
model.compile(optimizer = adam, loss = 'categorical_crossentropy', metrics = ['accuracy'])

x = np.array(x_train)
y = np.array(y_train)
model.save('botModel', model.fit(x, y, batch_size = 10, epochs = 400, verbose = 2))

print("Training complete!")
