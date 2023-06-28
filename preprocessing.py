import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import nltk
import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

# Variables
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
nltk.download('wordnet')
lemma=WordNetLemmatizer()
stemmer = PorterStemmer()

def clean_book_summaries(text):
  # remove apostrophe
  text = re.sub("\'", "", text)

  #removing punctuation
  text = re.sub('[%s]' % re.escape(string.punctuation), ' ',text)

  #removing single character
  text = re.sub(r"\s+[a-zA-Z]\s+", ' ', text)

  #removing HTML Tags
  text = re.sub('<.*?>+',' ',text)

  #removal of new line characters
  text = re.sub('\n', ' ',text)

  #removal of multiple spaces
  text = re.sub(r'\s+', ' ',text)

  #remove all punctuations except for alphabets
  text = re.sub("^a-zA-Z", " ", text)

  #removing whitespaces
  text = ' '.join(text.split())

  #convert text to lowercase
  text = text.lower()

  return text

# STOP WORDS REMOVAL
def remove_stopwords(text):
  text_removed_stopword = [x for x in text.split() if not x in stop_words]
  return ' '.join(text_removed_stopword)

# Lemmatization Function
def lemmatizer(sentence):
    sentence_stem = ""

    for word in sentence.split():
        stem = lemma.lemmatize(word)
        sentence_stem += stem
        sentence_stem += " "

    sentence_stem = sentence_stem.strip()

    return sentence_stem

# Stemming Function
def stemming(sentence):
    sentence_stem = ""
    for word in sentence.split():
        stem = stemmer.stem(word)
        sentence_stem += stem
        sentence_stem += " "

    sentence_stem = sentence_stem.strip()

    return sentence_stem