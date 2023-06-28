import string
from preprocessing import clean_book_summaries, remove_stopwords, lemmatizer, stemming
from sklearn.feature_extraction.text import TfidfVectorizer

def classification_process(data, vectorizer, model):

  data = clean_book_summaries(data)
  data = remove_stopwords(data)
  data = lemmatizer(data)
  data = stemming(data)
  data_vectorize = vectorizer.transform([data])
  sv_prediction = model.predict(data_vectorize)

  return sv_prediction