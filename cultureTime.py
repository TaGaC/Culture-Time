from flask import Flask, render_template, request, redirect, session, flash, url_for

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


@app.route("/dailyquestion", methods=["GET", "POST"])
def dailyquestion():
    # Récupérer la question du jour
    res = affichage_du_jour()
    titre = res[0][0]
    question = res[0][1]
    reponses = res[0][2].split(",")
    bonne_reponse = res[0][3]
    corps = res[0][4]
    source = res[0][5]
    return render_template("dailyquestion.html", title="Daily Question", question=question, reponses=reponses, bonne_reponse=bonne_reponse, corps=corps, source=source)

# Route pour la page "records"
@app.route("/records/<int:i>")
def records(i):
    # Récupérez toutes les anecdotes de la base de données
    i_anecdotes = get_anecdotes(i)
    # Rendez le modèle "records.html" en passant les données des anecdotes
    return render_template("records.html", title="Records", questions=i_anecdotes, i=i)


@app.route("/question/<int:i>", methods=["GET", "POST"])
def selected_question(i):
    # Récupérer la question choisie en fonction de son ID
    res = select_question_number(i)
    if res:
        titre = res[0][0]
        question = res[0][1]
        reponses = res[0][2].split(",")
        bonne_reponse = res[0][3]
        corps = res[0][4]
        source = res[0][5]
        date = res[0][6]
        return render_template("question.html", title="Question", question=question, reponses=reponses, bonne_reponse=bonne_reponse, corps=corps, source=source, date=date)
    else:
        # Gérer le cas où aucune question n'est trouvée pour l'ID donné
        return "Question not found", 404
    


if __name__ == "__main__":
    # Utiliser la base de données
    if (False):
        initDB()
    if (False):
        init_data()
    app.run(debug=True, host='0.0.0.0', port='8080')

