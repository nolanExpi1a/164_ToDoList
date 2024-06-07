"""Gestion des "routes" FLASK et des données pour les genres.
Fichier : gestion_genres_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFAjouterGenres
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFDeleteGenre
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFUpdateGenre
"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /genres_afficher
    
    Test : ex : http://127.0.0.1:5575/genres_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_genre_sel = 0 >> tous les genres.
                id_genre_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/genres_afficher/<string:order_by>/<int:id_genre_sel>", methods=['GET', 'POST'])
def genres_afficher(order_by, id_genre_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_genre_sel == 0:
                    strsql_genres_afficher = """SELECT ID_Evenement, Nom_Evenement, Date_Evenement, Lieu FROM t_calendrier ORDER BY ID_Evenement ASC"""
                    mc_afficher.execute(strsql_genres_afficher)
                elif order_by == "ASC":
                    valeur_id_genre_selected_dictionnaire = {"value_id_genre_selected": id_genre_sel}
                    strsql_genres_afficher = """SELECT ID_Evenement, Nom_Evenement, Date_Evenement, Lieu FROM t_calendrier WHERE ID_Evenement = %(value_id_genre_selected)s ORDER BY ID_Evenement ASC"""
                    mc_afficher.execute(strsql_genres_afficher, valeur_id_genre_selected_dictionnaire)
                else:
                    strsql_genres_afficher = """SELECT ID_Evenement, Nom_Evenement, Date_Evenement, Lieu FROM t_calendrier ORDER BY ID_Evenement DESC"""
                    mc_afficher.execute(strsql_genres_afficher)

                data_genres = mc_afficher.fetchall()

                print("data_genres ", data_genres, " Type : ", type(data_genres))

                if not data_genres and id_genre_sel == 0:
                    flash("""La table "t_genre" est vide. !!""", "warning")
                elif not data_genres and id_genre_sel > 0:
                    flash(f"Le genre demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données genres affichés !!", "success")

        except Exception as Exception_genres_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{genres_afficher.__name__} ; "
                                          f"{Exception_genres_afficher}")

    return render_template("genres/genres_afficher.html", data=data_genres)



"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /genres_ajouter
    
    Test : ex : http://127.0.0.1:5575/genres_ajouter
    
    Paramètres : sans
    
    But : Ajouter un genre pour un film
    
    Remarque :  Dans le champ "name_genre_html" du formulaire "genres/genres_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/genres_ajouter", methods=['GET', 'POST'])
def genres_ajouter_wtf():
    form = FormWTFAjouterGenres()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                nom_evenement = form.nom_evenement_wtf.data
                date_evenement = form.date_evenement_wtf.data
                lieu = form.lieu_wtf.data

                valeurs_insertion_dictionnaire = {"value_Nom_Evenement": nom_evenement,
                                                  "Value_date_evenement": date_evenement,
                                                  "Value_lieu": lieu}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_genre = """INSERT INTO t_calendrier (ID_Evenement, Nom_Evenement, Date_Evenement, lieu) 
                VALUES (NULL, %(value_Nom_Evenement)s, %(Value_date_evenement)s, %(Value_lieu)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_genre, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('genres_afficher', order_by='DESC', id_genre_sel=0))

        except Exception as Exception_genres_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{genres_ajouter_wtf.__name__} ; "
                                            f"{Exception_genres_ajouter_wtf}")

    return render_template("genres/genres_ajouter_wtf.html", form=form)



"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /genre_update
    
    Test : ex cliquer sur le menu "genres" puis cliquer sur le bouton "EDIT" d'un "genre"
    
    Paramètres : sans
    
    But : Editer(update) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_update_wtf" du formulaire "genres/genre_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/genre_update", methods=['GET', 'POST'])
def genre_update_wtf():
    id_genre_update = request.values['id_genre_btn_edit_html']
    form_update = FormWTFUpdateGenre()

    try:
        if form_update.validate_on_submit():
            name_genre_update = form_update.nom_genre_update_wtf.data
            date_genre_update = form_update.date_genre_update_wtf.data
            lieu_genre_update = form_update.lieu_genre_update_wtf.data

            valeur_update_dictionnaire = {
                "value_id_genre": id_genre_update,
                "value_name_genre": name_genre_update,
                "value_date_genre": date_genre_update,
                "value_lieu_genre": lieu_genre_update
            }

            str_sql_update_genre = """UPDATE t_calendrier SET 
                                      Nom_Evenement = %(value_name_genre)s, 
                                      Date_Evenement = %(value_date_genre)s, 
                                      Lieu = %(value_lieu_genre)s 
                                      WHERE ID_Evenement = %(value_id_genre)s"""
            with DBconnection() as conn_bd:
                conn_bd.execute(str_sql_update_genre, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")

            return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=id_genre_update))

        elif request.method == "GET":
            str_sql_select_genre = "SELECT ID_Evenement, Nom_Evenement, Date_Evenement, Lieu FROM t_calendrier WHERE ID_Evenement = %(value_id_genre)s"
            valeur_select_dictionnaire = {"value_id_genre": id_genre_update}
            with DBconnection() as conn_bd:
                conn_bd.execute(str_sql_select_genre, valeur_select_dictionnaire)
                data_genre = conn_bd.fetchone()

            form_update.nom_genre_update_wtf.data = data_genre["Nom_Evenement"]
            form_update.date_genre_update_wtf.data = data_genre["Date_Evenement"]
            form_update.lieu_genre_update_wtf.data = data_genre["Lieu"]

    except Exception as e:
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name}  ;  {genre_update_wtf.__name__} ; {e}")

    return render_template("genres/genre_update_wtf.html", form_update=form_update)





"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete
    
    Test : ex. cliquer sur le menu "genres" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_delete_wtf" du formulaire "genres/genre_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/genre_delete", methods=['GET', 'POST'])
def genre_delete_wtf():
    data_calendrier_attribue_genre_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_genre"
    id_genre_delete = request.values['id_genre_btn_delete_html']

    # Objet formulaire pour effacer le genre sélectionné.
    form_delete = FormWTFDeleteGenre()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("genres_afficher", order_by="ASC", id_genre_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "genres/genre_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_calendrier_attribue_genre_delete = session['data_calendrier_attribue_genre_delete']
                print("data_calendrier_attribue_genre_delete ", data_calendrier_attribue_genre_delete)

                flash(f"Effacer le genre de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_genre": id_genre_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_calendrier_genre = """DELETE FROM t_calendrier WHERE ID_Evenement = %(value_id_genre)s"""

                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_calendrier_genre, valeur_delete_dictionnaire)

                flash(f"Genre définitivement effacé !!", "success")
                print(f"Genre définitivement effacé !!")

                # afficher les données
                return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_genre": id_genre_delete}
            print(id_genre_delete, type(id_genre_delete))

            # Requête qui affiche tous les événements qui ont le genre que l'utilisateur veut effacer
            str_sql_genres_calendrier_delete = """SELECT ID_Evenement, Nom_Evenement FROM t_calendrier 
                                                  WHERE ID_Evenement = %(value_id_genre)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_genres_calendrier_delete, valeur_select_dictionnaire)
                data_calendrier_attribue_genre_delete = mydb_conn.fetchall()
                print("data_calendrier_attribue_genre_delete...", data_calendrier_attribue_genre_delete)

                session['data_calendrier_attribue_genre_delete'] = data_calendrier_attribue_genre_delete

                str_sql_id_genre = "SELECT ID_Evenement, Nom_Evenement FROM t_calendrier WHERE ID_Evenement = %(value_id_genre)s"

                mydb_conn.execute(str_sql_id_genre, valeur_select_dictionnaire)
                data_nom_genre = mydb_conn.fetchone()
                print("data_nom_genre ", data_nom_genre, " type ", type(data_nom_genre), " genre ",
                      data_nom_genre["Nom_Evenement"])

            form_delete.nom_genre_delete_wtf.data = data_nom_genre["Nom_Evenement"]

            btn_submit_del = False

    except Exception as Exception_genre_delete_wtf:
        raise ExceptionGenreDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{genre_delete_wtf.__name__} ; "
                                      f"{Exception_genre_delete_wtf}")

    return render_template("genres/genre_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_calendrier_associes=data_calendrier_attribue_genre_delete)


