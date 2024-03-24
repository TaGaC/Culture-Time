from flask import Flask, render_template, request, redirect, session, flash
from flask_session import Session

from functions import *


# flask app creation
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = '35a66b836297c6d61b8e68b287fe44fadb0d7c2d24b8d378890c09d30fcf7a89'
Session(app)


#def des routes:
 
#/home (max)
@app.route("/")
def home():
    return render_template("home.html", title = "CultureTime")

@app.route("/sign-in")
def sign_in():
    return render_template("sign-in.html", title = "Sign In")

@app.route("/sign-up")
def sign_up():
    return render_template("sign-up.html", title = "Sign Up")

@app.route("/profile")
def profile():
    return render_template("profile.html", title = "Profile")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='8080')

