import codecs
import os, pickle
import io
import matplotlib.pyplot as plt
from ssl import AlertDescription
import gridfs

from bson.objectid import ObjectId

# from flask_pymongo import PyMongo

# import cloudinary
# from cloudinary import uploader
# import config

from werkzeug.utils import secure_filename
from bson.binary import Binary

from PIL import Image

from pprint import pprint

from predictions import classification_process

from flask import Flask, flash,render_template, request, redirect, url_for

from pymongo import MongoClient

# Create object using flask
app = Flask(__name__)
app.secret_key = "alexandrea"

## This is for PyMongo Config of flask_pymongo
# app.config["MONGO_URI"] = os.getenv("MONGO_URI")
# app.config["MONGO_URI"] = 'mongodb://localhost:27017'
# mongo = PyMongo(app)
# pymongo = PyMongo(app)

## This is MongoClient config of pymongo
# # This URI connects in which mongodb server you are located, first is in the atlas (web), second is local
# uri = "mongodb+srv://jfsolivar:rw3wplVA6701T4gd@alexandria.9mrd2oe.mongodb.net/?retryWrites=true&w=majority"
uri = "mongodb://localhost:27017"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client['lms-dev']
records = db.books
grid_fs = gridfs.GridFS(db)

## This is for ensuring the connection of the database
# # List all the databases in the cluster:
# for db_info in client.list_database_names():
#    print(db_info)

# # List all the collections in 'lms_dev':
# collections = db.list_collection_names()
# for collection in collections:
#    print(collection)

# # Get a reference to the 'books' collection: 
# books = db['books']

# # Get a document with the genre 'fantasy':
# pprint(books.find_one({'genre': 'fantasy'}))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# Load the TF-IDF vectorizer and svm model
load_vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))
svm_model = pickle.load(open('models/svm-76-accuracy.pkl', 'rb'))

@app.route('/')
def home():
    pipeline = [
        {"$sample":{"size":6}}
    ]
    # some_book_with_image = records.distinct("img")
    # pprint(some_book_with_image)
    # pil_img = Image.open(io.BytesIO(some_book_with_image["img"]))
    # plt.imshow(pil_img)
    # plt.show()
    #pil_image = Image.open(io.BytesIO(some_book_with_image))
    #fp.seek(0)
    ##pic = url_for('img', img = some_book_with_image['img'])
    ##some_book_with_image['img'] = pic

    items = records.find().limit(3)
    images= []
    for item in items:
        image = grid_fs.get(item['id'])
        base64_data = codecs.encode(image.read(), 'base64')
        image = base64_data.decode('utf-8')
        images.append({
            "image" : image 
            })

    # image = grid_fs.get(item['id'])
    # base64_data = codecs.encode(image.read(), 'base64')
    # image = base64_data.decode('utf-8')

    some_books = records.aggregate(pipeline)

    return render_template("home.html", some_books = some_books, images=images)

@app.route('/sidebar')
def sidebar():
    return render_template("sidebar.html")

@app.route('/<id>/delete')
def delete(id):
    records.delete_one({"_id": ObjectId(id)})
    flash('Successfully deleted a book.', 'delete')
    return redirect(url_for('books'))

@app.route('/books')
def books():
    all_books = records.find()
    return render_template("books.html", all_books=all_books)

@app.route('/analytics')
def analytics():
    return render_template("analytics.html")

@app.route('/genre-checker')
def genre_checker():
    return render_template("genre-checker.html")

@app.route('/add-books', methods=["GET", "POST"])
def add_books():
        # For GET request: Display form for user to submit report of UFO sighting
    if request.method == "GET":
        return render_template("add-books.html")
    
    books = {}

    # should not exeed 16mb
    book_image = request.files['img']
    
    # name = book_image.filename
    # name = name.replace(" ", "")
    # book_image.save(secure_filename(name))

    # with open(name, "rb") as hoja:
    #     encoded = Binary(hoja.read())

    # imgByteArr = io.BytesIO()
    # book_image.save(imgByteArr)

    book_title = request.form.get("book-title")
    book_author = request.form.get("book-author")
    pub_year = request.form.get("pub-year")
    summary = request.form.get("summary")
    genre = request.form.get("genre")
    id = grid_fs.put(book_image, content_type = book_image.content_type, 
                     filename = book_title)

    books["id"] = id #encoded #imgByteArr.getvalue()
    books["title"] = book_title
    books["book_author"] = book_author
    books["pub_year"] = pub_year
    books["summary"] = summary
    books["genre"] = genre

    pprint(books)
    records.insert_one(books)

    flash('You successfully added a new book!', 'add')

    return redirect(url_for('books'))

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    summary = request.args.get('summary')
    if request.method == 'POST':
        summary = request.get_data()
    
    # pass to the preprocessing and classification method
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
