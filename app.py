from cs50 import SQL
from flask import Flask, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///words.db")

@app.route("/")
def index():
    words = db.execute("SELECT * FROM words")
    return render_template("index.html", words=words)
    
@app.route("/filter")
def filter():
    word = request.args.get("sWord")
    sWords = db.execute("SELECT * FROM words WHERE word LIKE ?", word + "%")
    return render_template("index.html", words=sWords)