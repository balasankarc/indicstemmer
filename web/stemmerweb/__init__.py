from flask import Flask


app = Flask(__name__)
from stemmerweb import views
