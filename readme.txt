Pour lancer l'application:

Lancer un environnement virtuel:

Création de l'environnement virtuel:
python3 -m venv env   

Activation de l'environnement virtuel:
source env/bin/activate

Désactivation de l'environnement virtuel:
deactivate


Ajouter tous les requirements utiles:
pip install -r requirements.txt

Mettre a jour la liste des requirements:
pip freeze > requirements.txt


Pour lancer le serveur:
export FLASK_APP=cultureTime.py
flask run


Pour acceder au site:
http://192.168.1.143:8080/
