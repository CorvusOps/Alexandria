import os
from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
