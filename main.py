#!/usr/bin/env python3

# import libraries

import pandas as pd
import numpy as np
import nltk
import csv
import string
import re

from collections import Counter
from nltk.collocations import *
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from stop_words import get_stop_words

# upload .csv file with recent tweets

path ='\trump.csv'
data = pd.read_csv(path)
print(data)

# data preparation, drop colums exept for date and text

new_data = data.drop(['created_at', 'retweet_count', 'favorite_count', 'is_retweet', 'id_str', 'time'], axis=1)
data[['date','time']] = data.created_at.str.split(expand=True) 

# tokenising words and sentances

data['text'] = data['text'].astype('str')
data['text_word_tokenized'] = data['text'].apply(word_tokenize)
data['text_sent_tokenized'] = data['text'].apply(sent_tokenize)

# grouping data
word_data_grouped = word_data.groupby("date")['text_word_tokenized'].apply(list)
sent_data_grouped = sent_data.groupby("date")['text_sent_tokenized'].apply(list)

# top most freqient words for the period

def content_text(text):
    stopwords = list(get_stop_words('en'))
    with_stp = Counter()
    without_stp  = Counter()
    with open(text, errors='ignore') as f:
        for line in f:
            spl = line.split()
            # update count off all words in the line that are in stopwrods
            with_stp.update(w.lower().rstrip(punctuation) for w in spl if w.lower() in stopwords)
               # update count off all words in the line that are not in stopwords
            without_stp.update(w.lower().rstrip(punctuation)  for w in spl if w  not in stopwords)
    # return a list with top 20 most common words from each 
    return [x for x in with_stp.most_common(20)],[y for y in without_stp.most_common(100)]

wth_stop, wthout_stop = content_text('C:\\Users\\kunas\\PycharmProjects\\Trump\\06-2017_sent.txt')
print(wthout_stop)


# saving the results to the file
np.savetxt("popular_words.csv", wthout_stop, delimiter=",", fmt='%s')


test_tokens = list(nltk.corpus.gutenberg.words("C:\\Users\\kunas\\PycharmProjects\\Trump\\06-2017_sent.txt")) # note the use of words() to load tokens
test_words = [word for word in test_tokens if word[0].isalpha()] # filter out non-words
print(test_words[:25])


test_text = nltk.Text(test_words)
test_text.collocation_list(30) # 30 top bigrams separated by semi-colon


test_text_grams = list(nltk.ngrams(test_words, 3)) # create three-grams
test_text_grams_freqs = nltk.FreqDist(test_text_grams) # determine frequency of three-grams
for words, count in test_text_grams_freqs.most_common(30): # for the 30 most common three-grams
    print(count, " ".join(list(words))) # show the count and the create a string from the tuple


test_text_grams = list(nltk.ngrams(test_words, 2)) # create two-grams
test_text_grams_freqs = nltk.FreqDist(test_text_grams) # determine frequency of two-grams
for words, count in test_text_grams_freqs.most_common(100): # for the 30 most common two-grams
    print(count, " ".join(list(words))) # show the count and the create a string from the tuple


with open('C:\\Users\\kunas\\PycharmProjects\\Trump\\06-2017_sent.txt', errors='ignore') as f:
    passage = f.read()
    
stopwords = list(get_stop_words('en'))
words = re.findall(r'\w+', passage)

cap_words = [word.upper() for word in words]

word_counts = Counter(cap_words)


print(word_counts)

