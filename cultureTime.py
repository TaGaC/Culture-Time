from flask import Flask, render_template, request, redirect, session, flash, url_for

from flask_session import Session

from functions import *


# flask app creation
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = '35a66b836297c6d61b8e68b287fe44fadb0d7c2d24b8d378890c09d30fcf7a89'
Session(app)

# Liste des questions et réponses
questions = [
    {
        "question": "Does the UK have a Prime Minister?",
        "correct_answer": "True",
        "explanation": "The United Kingdom has a parliamentary system of government, in which the Prime Minister is the head of government. The Prime Minister is appointed by the monarch and is usually the leader of the political party with the most seats in the House of Commons."
    }
    # Ajoutez d'autres questions ici au besoin
]

# Utiliser la base de données
initdb()
init_data()
cursor, db = connectdb()

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


@app.route("/dailyquestion", methods=["GET", "POST"])
def dailyquestion():
    # Récupérer la question du jour
    res = affichage_du_jour()
    titre = res[0]
    question = res[1]
    reponses = res[2]
    bonne_reponse = res[3]
    corps = res[4]
    source = res[5]
    return render_template("dailyquestion.html", title="Daily Question", question=today_question, correct_answer=correct_answer)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='8080')

