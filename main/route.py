from main import app
from flask import render_template, url_for
from main.form import loginForm, registrationForm

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    form = loginForm()
    return render_template("login.html", form = form)

@app.route("/register", methods=["GET","POST"])
def register():
    form = registrationForm()
    return render_template("register.html", form = form)

@app.route("/account")
def account():
    return render_template("account.html")