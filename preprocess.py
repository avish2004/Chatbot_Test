import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import json
from sklearn.preprocessing import LabelEncoder

lemmatizer = WordNetLemmatizer()

def preprocess_data(data):
    words = []
    classes = []
    documents = []
    ignore_words = ['?', '!']

    for intent in data['intents']:
        for pattern in intent['patterns']:
            word_list = nltk.word_tokenize(pattern)
            words.extend(word_list)
            documents.append((word_list, intent['tag']))
            if intent['tag'] not in classes:
                classes.append(intent['tag'])

    words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
    words = sorted(list(set(words)))
    classes = sorted(list(set(classes)))

    training = []
    output = []
    output_empty = [0] * len(classes)

    for doc in documents:
        bag = []
        word_patterns = doc[0]
        word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
        for w in words:
            bag.append(1) if w in word_patterns else bag.append(0)
        
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1

        training.append(bag)
        output.append(output_row)

    training = np.array(training)
    output = np.array(output)

    return words, classes, documents, training, output
