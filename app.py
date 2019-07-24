from flask import Flask
from flask import render_template
from flask import request
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
static_folder_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "client")
bootstrap = Bootstrap(app)


@app.route("/")
def home():
   return "Welcome to Pinolo's Journey"

@app.route("/playsonars")
def register():
   content = "Register Time"
   return render_template("index.html")
   # return "Register!"
