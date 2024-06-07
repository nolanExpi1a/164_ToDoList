from pathlib import Path
from flask import redirect, request, session, url_for, flash, render_template
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.contrats.gestion_contrats_wtf_forms import FormeWTFajouterContrats, FormWTFdeleteContrats, FormWTFupdateContrats

@app.route("/gestion_contrats_afficher/<string:order_by>/<int:id_contrat_sel>", methods=['GET', 'POST'])
def gestion_contrats_afficher(order_by, id_contrat_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_contrat_sel == 0:
                    strsql_contrats_afficher = """SELECT ID_Contrat, ID_Artiste, Date_Contrat, Description_Contrat, Montant FROM t_contrats ORDER BY ID_Contrat ASC"""
                    mc_afficher.execute(strsql_contrats_afficher)
                elif order_by == "ASC":
                    valeur_id_contrat_selected_dictionnaire = {"value_id_contrat_selected": id_contrat_sel}
                    strsql_contrats_afficher = """SELECT ID_Contrat, ID_Artiste, Date_Contrat, Description_Contrat, Montant FROM t_contrats WHERE ID_Contrat = %(value_id_contrat_selected)s ORDER BY ID_Contrat ASC"""
                    mc_afficher.execute(strsql_contrats_afficher, valeur_id_contrat_selected_dictionnaire)
                else:
                    strsql_contrats_afficher = """SELECT ID_Contrat, ID_Artiste, Date_Contrat, Description_Contrat, Montant FROM t_contrats ORDER BY ID_Contrat DESC"""
                    mc_afficher.execute(strsql_contrats_afficher)

                data_contrats = mc_afficher.fetchall()

                if not data_contrats:
                    flash("Aucun contrat trouvé", "warning")

        except Exception as Exception_contrats_afficher:
            raise ExceptionContratsAfficher(f"fichier : {Path(__file__).name}  ;  "
                                            f"{gestion_contrats_afficher.__name__} ; "
                                            f"{Exception_contrats_afficher}")

    return render_template("contrats/gestion_contrats_afficher.html", data=data_contrats)


@app.route("/gestion_contrats_add_wtf", methods=['GET', 'POST'])
def gestion_contrats_add_wtf():
    form = FormeWTFajouterContrats()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                nom_contrat = form.nom_contrat_wtf.data
                date_contrat = form.date_contrat_wtf.data
                lieu_contrat = form.lieu_contrat_wtf.data

                valeurs_insertion_dictionnaire = {"value_nom_contrat": nom_contrat,
                                                  "value_date_contrat": date_contrat,
                                                  "value_lieu_contrat": lieu_contrat}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_contrat = """INSERT INTO t_contrats (ID_Contrat, ID_Artiste, Date_Contrat, Description_Contrat, Montant) 
                VALUES (NULL, %(value_nom_contrat)s, %(value_date_contrat)s, %(value_lieu_contrat)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_contrat, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('gestion_contrats_afficher', order_by='DESC', id_contrat_sel=0))

        except Exception as Exception_contrats_ajouter_wtf:
            raise ExceptionContratsAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{gestion_contrats_add_wtf.__name__} ; "
                                            f"{Exception_contrats_ajouter_wtf}")

    return render_template("contrats/contrats_ajouter_wtf.html", form=form)

@app.route("/gestion_contrats_update_wtf/<int:id_contrat_update>", methods=['GET', 'POST'])
def gestion_contrats_update_wtf(id_contrat_update):
    form_update = FormWTFupdateContrats()

    try:
        if form_update.validate_on_submit():
            nom_contrat_update = form_update.nom_contrat_update_wtf.data
            date_contrat_update = form_update.date_contrat_update_wtf.data
            lieu_contrat_update = form_update.lieu_contrat_update_wtf.data

            valeur_update_dictionnaire = {
                "value_id_contrat": id_contrat_update,
                "value_nom_contrat": nom_contrat_update,
                "value_date_contrat": date_contrat_update,
                "value_lieu_contrat": lieu_contrat_update
            }

            str_sql_update_contrat = """UPDATE t_contrats SET 
                                      Nom_Contrat = %(value_nom_contrat)s, 
                                      Date_Contrat = %(value_date_contrat)s, 
                                      Lieu_Contrat = %(value_lieu_contrat)s 
                                      WHERE ID_Contrat = %(value_id_contrat)s"""
            with DBconnection() as conn_bd:
                conn_bd.execute(str_sql_update_contrat, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")

            return redirect(url_for('gestion_contrats_afficher', order_by='ASC', id_contrat_sel=id_contrat_update))

        elif request.method == "GET":
            str_sql_select_contrat = "SELECT ID_Contrat, ID_Artiste, Date_Contrat, Description_Contrat, Montant FROM t_contrats WHERE ID_Contrat = %(value_id_contrat)s"
            valeur_select_dictionnaire = {"value_id_contrat": id_contrat_update}
            with DBconnection() as conn_bd:
                conn_bd.execute(str_sql_select_contrat, valeur_select_dictionnaire)
                data_contrat = conn_bd.fetchone()

            form_update.nom_contrat_update_wtf.data = data_contrat["Nom_Contrat"]
            form_update.date_contrat_update_wtf.data = data_contrat["Date_Contrat"]
            form_update.lieu_contrat_update_wtf.data = data_contrat["Lieu_Contrat"]

    except Exception as e:
        raise ExceptionContratUpdateWtf(f"fichier : {Path(__file__).name}  ;  {gestion_contrats_update_wtf.__name__} ; {e}")

    return render_template("contrats/contrat_update_wtf.html", form_update=form_update)

@app.route("/gestion_contrats_delete_wtf/<int:id_contrat_delete>", methods=['GET', 'POST'])
def gestion_contrats_delete_wtf(id_contrat_delete):
    data_contrats_attribue_contrat_delete = None
    btn_submit_del = None

    form_delete = FormWTFdeleteContrats()
    try:
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("gestion_contrats_afficher", order_by="ASC", id_contrat_sel=0))

            if form_delete.submit_btn_conf_del.data:
                data_contrats_attribue_contrat_delete = session['data_contrats_attribue_contrat_delete']
                flash(f"Effacer le contrat de façon définitive de la BD !!!", "danger")
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_contrat": id_contrat_delete}

                str_sql_delete_contrat = """DELETE FROM t_contrats WHERE ID_Contrat = %(value_id_contrat)s"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_contrat, valeur_delete_dictionnaire)

                flash(f"Contrat définitivement effacé !!", "success")

                return redirect(url_for('gestion_contrats_afficher', order_by="ASC", id_contrat_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_contrat": id_contrat_delete}

            str_sql_contrats_attribue_contrat_delete = """SELECT * FROM t_contrats WHERE ID_Contrat = %(value_id_contrat)s"""
            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_contrats_attribue_contrat_delete, valeur_select_dictionnaire)
                data_contrats_attribue_contrat_delete = mydb_conn.fetchall()

                session['data_contrats_attribue_contrat_delete'] = data_contrats_attribue_contrat_delete

                str_sql_id_contrat = "SELECT ID_Contrat, ID_Artiste, Date_Contrat, Description_Contrat, Montant FROM t_contrats WHERE ID_Contrat = %(value_id_contrat)s"
                mydb_conn.execute(str_sql_id_contrat, valeur_select_dictionnaire)
                data_contrat = mydb_conn.fetchone()

                form_delete.nom_contrat_delete_wtf.data = data_contrat["Nom_Contrat"]
                form_delete.date_contrat_delete_wtf.data = data_contrat["Date_Contrat"]
                form_delete.lieu_contrat_delete_wtf.data = data_contrat["Lieu_Contrat"]

            btn_submit_del = False

    except Exception as e:
        raise ExceptionContratDeleteWtf(f"fichier : {Path(__file__).name}  ;  {gestion_contrats_delete_wtf.__name__} ; {e}")

    return render_template("contrats/contrat_delete_wtf.html", form_delete=form_delete, btn_submit_del=btn_submit_del, data_contrats_associes=data_contrats_attribue_contrat_delete)
