from cs50 import SQL
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

db = SQL("sqlite:///words.db")

@app.route("/")
def index():
    words = db.execute("SELECT * FROM words")
    return render_template("index.html", words=words)

@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("login-name")
    users = db.execute("SELECT username FROM users WHERE user_type_id = 1")
    if not name:
        return render_template("error.html", message="Missing user")
    for user in users:
        if name not in user["username"]:
            return render_template("error.html", message="User not in Database")
        else:
            return render_template("success.html")
    

@app.route("/filter")
def filter():
    q = request.args.get("sWord")
    if q != "":
        sWords = db.execute("SELECT * FROM words WHERE word LIKE ?", q + "%")
    else:
        sWords = db.execute("SELECT * FROM words")
    return render_template("filter.html", words=sWords)