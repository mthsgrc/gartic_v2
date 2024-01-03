from cs50 import SQL
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

db = SQL("sqlite:///words.db")

@app.route("/")
def index():
    words = db.execute("SELECT * FROM words")
    return render_template("index.html", words=words)
    
@app.route("/filter")
def filter():
    q = request.args.get("sWord")
    if q != "":
        sWords = db.execute("SELECT * FROM words WHERE word LIKE ?", q + "%")
    else:
        sWords = db.execute("SELECT * FROM words")
    return render_template("filter.html", words=sWords)