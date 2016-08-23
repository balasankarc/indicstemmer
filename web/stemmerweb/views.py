import sys
import os
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            __file__,
            '../../../libindic')))
from stemmer import Malayalam as Stemmer
from flask import request, render_template
import json

from stemmerweb import app


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/api/stem", methods=['GET', 'POST'])
def inflect():
    word = request.form['word'].strip()
    result = None
    if word:
        mlstemmer = Stemmer()
        result = mlstemmer.stem(word)
        if not result:
            result = "Error"
        output = {}
        output[word] = result[word]
        return json.dumps(output)
    else:
        return word
