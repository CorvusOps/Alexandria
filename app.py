import os, pickle
from predictions import classification_process

from flask import Flask, render_template, request

# Create object using flask
app = Flask(__name__)

# Load the TF-IDF vectorizer and svm model
load_vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))
svm_model = pickle.load(open('models/svm-76-accuracy.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/sidebar')
def sidebar():
    return render_template("sidebar.html")

@app.route('/books')
def books():
    return render_template("books.html")

@app.route('/analytics')
def analytics():
    return render_template("analytics.html")

@app.route('/genre-checker')
def genre_checker():
    return render_template("genre-checker.html")

@app.route('/add-books')
def add_books():
    return render_template("add-books.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    summary = request.args.get('summary')
    if request.method == 'POST':

        summary = request.get_data()
    # print(data)
    prediction_output = classification_process(summary, load_vectorizer, svm_model)
    if prediction_output == 0:
        pred_label = 'Fantasy'
    elif prediction_output == 1:
        pred_label = 'History'
    elif prediction_output == 2:
        pred_label = 'Horror'
    elif prediction_output == 3:
        pred_label = 'Science'
    elif prediction_output == 4:
        pred_label = 'Thriller'
        
    return pred_label

if __name__ == '__main__':
    app.run(debug=True, port=5000)
