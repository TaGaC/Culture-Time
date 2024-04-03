import sqlite3
from datetime import date
import requests
from hashlib import sha512



# ATTENTION : les variables suivantes peuvent supprimer la bd. a manier en phase de test
reset_db = False
phase_tests = False


# fonction permettant de créer un cruseur pour naviguer dans la base de donnée.
def connectdb():
    db = sqlite3.connect('cultureTime.db')
    cursor = db.cursor()
    return db, cursor


def requete_db_avec_reponse(query, args):
    '''fonction prenant pour arguments query, une requête SQL et args, les arguments de celle-ci, 
    renvoyant res correspondant à une liste de tuples correspondants aux lignes de la query.'''

    db, cursor = connectdb()
    if args == ():
        cursor.execute(query)
    else:
        cursor.execute(query, args)
    res = cursor.fetchall()
    db.commit()
    cursor.close()
    db.close()
    return res


def requete_db_sans_reponse(query, args):
    '''fonction ayant la même fonctionnalité que requete_db_avec_reponse mais pour les requêtes SQL 
    ne renvoyant rien ex : UPDATE'''
    db, cursor = connectdb()
    if args == ():
        cursor.execute(query)
    else:
        cursor.execute(query, args)
    db.commit()
    cursor.close()
    db.close()

def initdb():
    # Fonction créant la base de donnée, chaque tables et chaque colonnes de celles-ci
    query = '''DROP TABLE IF EXISTS Anecdotes;
    CREATE TABLE Anecdotes (
	    id_anecdote	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        date	INTEGER NOT NULL,
        auteur	TEXT NOT NULL,
        titre	TEXT NOT NULL,
        question TEXT NOT NULL,
        reponses TEXT NOT NULL,
        bonne_reponse TEXT NOT NULL,
        corps	TEXT NOT NULL,
        source    TEXT,
        image TEXT,
        categorie INTEGER NOT NULL,
        FOREIGN KEY (categorie) REFERENCES Categories(id_categorie)
    );

    DROP TABLE IF EXISTS Categories;
    CREATE TABLE Categories (
        id_categorie	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        nom	TEXT NOT NULL,
        nombre_anecdotes	INTEGER NOT NULL
    );

        '''
    db, cursor = connectdb()
    cursor.executescript(query)
    db.commit()
    cursor.close()
    db.close()

def init_data():
    # Fonction ajoutant les données d'un csv dans la BD
    f = open('data/data.csv', 'r')
    F = f.readlines()
    for k in range(len(F)):
        l = F[k].strip().split(';')
        query = '''INSERT INTO Anecdotes (date, auteur, titre, question, reponses, bonne_reponse, corps, source, image, categorie) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        args = (l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9])
        requete_db_sans_reponse(query, args)
    f.close()

    f = open('data/categories.csv', 'r')
    F = f.readlines()
    for k in range(len(F)-1):
        l = F[k].strip().split(';')
        query = '''INSERT INTO Categories (nom, nombre_anecdotes) VALUES (?, ?)'''
        args = (l[0], l[1])
        requete_db_sans_reponse(query, args)
    f.close()

def save_data(data):
    # Fonction ajoutant une anecdote dans la BD
    query = '''INSERT INTO Anecdote (date, auteur, titre, question, reponses, bonne_reponse, corps, source, image, categorie) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    requete_db_sans_reponse(query, data)

def affichage_anecdotes(catagorie):
    # Fonction renvoyant une liste de tuples correspondant à toutes les anecdotes de la BD de la catégorie donnée
    # Cette fonction ne renvoit que le titre, l'auteur, la description et la date

    query = '''SELECT titre, auteur, description, date FROM Anecdotes WHERE categorie = ?'''
    args = (catagorie)
    res = requete_db_avec_reponse(query, args)
    return res

def affichage_anecdote(id_anecdote):
    # Fonction renvoyant une liste de tuples correspondant à l'anecdote de la BD dont l'id est donné
    # Cette fonction renvoit toutes les informations sur l'anecdote

    query = '''SELECT * FROM Anecdotes WHERE id_anecdote = ?'''
    args = (id_anecdote)
    res = requete_db_avec_reponse(query, args)
    return res

def affichage_du_jour():
    # Fonction renvoyant une liste de tuples correspondant à l'anecdote du jour
    # Cette fonction ne renvoit que le titre, l'auteur, la description et la date
    query = '''SELECT titre, question, reponses, bonne_reponse, corps, source, date FROM Anecdotes WHERE date = ?'''
    args = (date.today().strftime('%Y%m%d'))
    res = requete_db_avec_reponse(query, args)
    return res