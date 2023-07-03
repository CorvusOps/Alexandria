# Alexandria
[!['Open Colab'](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1nnt40Ho98irHQ8fVvElLt6c3F1y9wDfX?usp=sharing)
---
Automated Book Categorization, Labeling, and Classification base on Synopsis/Abstract/Book Description

# Requirements
1. [MongoDB](https://docs.mongodb.com/manual/installation/) -  is a NoSQL document-oriented database program that uses JSON-like documents with optional schemas. Used in this project as the main database to store the results of the Trained Model.
2. [Python](https://www.python.org/downloads/) - is an interpreted high-level programming language for general-purpose programming. Used as the main language on building both web and the models.
3. [Node.js](https://nodejs.org/en/download) -  is an open-source, cross-platform, back-end JavaScript runtime environment that runs on the V8 engine and executes JavaScript code outside a web browser. Used in this project to beautify the web in consideration of the runtime environment.
4. [NPM](https://docs.npmjs.com/getting-started) - is the package manager for the Node.js JavaScript runtime environment. Used in this project to add dependencies on different modules.
5. [OpenColab](https://colab.research.google.com/notebooks/intro.ipynb) - is a free online platform that allows you to write and run Python code in your browser. Used in this project to do the Exploratory Data Analysis, Training and Testing of the Model and more. 

## Project Set-up
1. Clone the Repository.
```
git clone https://github.com/CorvusOps/Alexandria.git
```

2. Create Virtual Environment inside the Project Folder.
```bash
#Linux and Mac
python -m venv venv

#windows users
python -m venv c:\path\to\myenv

## Or run it via vs code 
# -> ctrl + shift + p
# -> Python: Create Environment
# -> Choose 'venv'
# -> Select interpreter 'python 3.xx.x'
# -> Select dependencies to install 'requirement.txt'

```

3. Activate the virtual environment.
```bash
# Linux and Mac
source venv/bin/activate

#Windows users
\venv\Scripts\activate.bat
```

4. Install all the project dependencies.
```bash
pip install -r requirment.txt
```

5. Start the Application (you can run it via vs code by run and debug then choosing flask).
```bash
# Run the application
export FLASK_APP="app.py";
export FLASK_DEBUG="True"
flask run;  # 127.0.0.1:5000

## Then you would see 
# Pinged your deployment. You successfully connected to MongoDB!
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

