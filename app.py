from cs50 import SQL
from flask import Flask, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///words.db")

@app.route("/")
def index():
    words = db.execute("SELECT * FROM words")
    return render_template("index.html", words=words)