import pandas as pd
import spacy
import re
import numpy as np
from sklearn.svm import SVC

data = "archive/Tweets.csv"
data_read = pd.read_csv(data)

# print(data_read.columns)
tweets = []
sentiments = []

### loading tweets and sentiments to tweets and sentiments list ###
### tokenizing the data ###
nlp = spacy.load("en_core_web_sm")
row = len(data_read)
i = 0

while(i < 10):
    text = data_read.iloc[i][10]
    doc = nlp(text)
    tokens = []
    for token in doc:
        tokens.append(token)
    tweets.append(tokens)
    i += 1

j = 0
while(j < 10):
    sentiments.append(data_read.iloc[j][1])
    j += 1

### punctuation removal ###
print(tweets[2])
i = 0
while(i<10):
    for item in tweets[i]:
        if item.is_punct:
            tweets[i].remove(item)
    i += 1

print(tweets[2])


### stopword removal ###
i = 0
while(i < 10):
    for item in tweets[i]:
        if item.is_stop:
            tweets[i].remove(item)
    i += 1
print(tweets[2])

### lemmatization ###
i = 0
lemmatized_tokens = []
while(i < 10):
    lemmatized = []
    for item in tweets[i]:
        lemmatized.append(item.lemma_)
    lemmatized_tokens.append(lemmatized)
    i += 1
print(lemmatized_tokens[2])


### lowercase ###
i = 0
while(i<10):
    for item in lemmatized_tokens[i]:
        lemmatized_tokens[i][lemmatized_tokens[i].index(item)] = item.lower()
    i += 1
print(lemmatized_tokens[2])

### removal of symbols and digits
i = 0
while(i<10):
    for item in lemmatized_tokens[i]:
        x = re.sub(r"[^A-Za-z@]", "", item)
        lemmatized_tokens[i][lemmatized_tokens[i].index(item)] = x
    i += 1
i = 0
while (i < 10):
    for item in lemmatized_tokens[i]:
        x = re.sub(r"[0-9]", "", item)
        lemmatized_tokens[i][lemmatized_tokens[i].index(item)] = x
    i += 1
i = 0
while (i < 10):
    for item in lemmatized_tokens[i]:
        x = re.sub(r'@\S+', '', item)
        lemmatized_tokens[i][lemmatized_tokens[i].index(item)] = x
    i += 1
i = 0
while (i < 10):
    for item in lemmatized_tokens[i]:
        x = re.sub(r'\S@\S+', '', item)
        lemmatized_tokens[i][lemmatized_tokens[i].index(item)] = x
    i += 1
i = 0
while (i < 10):
    for item in lemmatized_tokens[i]:
        x = re.sub(r'\S+com', "", item)
        lemmatized_tokens[i][lemmatized_tokens[i].index(item)] = x
    i += 1
i = 0
while (i < 10):
    for item in lemmatized_tokens[i]:
        if(item == "" or item == ''):
            lemmatized_tokens[i].remove(item)
    i += 1




z = np.array()
x = np.array(lemmatized_tokens)
y = np.array(sentiments)



print(x)
print(z)