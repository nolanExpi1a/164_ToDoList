from pathlib import Path
from flask import redirect, request, session, url_for, flash, render_template
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.contrats.gestion_contrats_wtf_forms import FormeWTFajouterContrats, FormWTFdeleteContrats, FormWTFupdateContrats

@app.route("/gestion_contrats_afficher/<string:order_by>/<int:id_contrat_sel>", methods=['GET', 'POST'])
def gestion_contrats_afficher(order_by, id_contrat_sel):
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

    except Exception as e:
        raise ExceptionContratsAfficher(f"fichier : {Path(__file__).name} ; {gestion_contrats_afficher.__name__} ; {str(e)}")

    return render_template("contrats/gestion_contrats_afficher.html", data=data_contrats)


@app.route("/gestion_contrats_add_wtf", methods=['GET', 'POST'])
def gestion_contrats_add_wtf():
    form = FormeWTFajouterContrats()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                values = {
                    "ID_Artiste": form.id_artiste_wtf.data,
                    "Date_Contrat": form.date_contrat_wtf.data,
                    "Description_Contrat": form.description_contrat_wtf.data,
                    "Montant": form.montant_wtf.data
                }
                strsql_insert_contrat = """INSERT INTO t_contrats (ID_Contrat, ID_Artiste, Date_Contrat, Description_Contrat, Montant) VALUES (NULL, %(ID_Artiste)s, %(Date_Contrat)s, %(Description_Contrat)s, %(Montant)s)"""
                with DBconnection() as conn:
                    conn.execute(strsql_insert_contrat, values)
                flash("Contrat ajouté avec succès", "success")
                return redirect(url_for('gestion_contrats_afficher', order_by="ASC", id_contrat_sel=0))

        except Exception as e:
            raise ExceptionContratsAjouterWtf(f"fichier : {Path(__file__).name} ; {gestion_contrats_add_wtf.__name__} ; {str(e)}")

    return render_template("contrats/gestion_contrats_add_wtf.html", form=form)



@app.route("/gestion_contrats_update_wtf/<int:id_contrat_update>", methods=['GET', 'POST'])
def gestion_contrats_update_wtf(id_contrat_update):
    form_update = FormWTFupdateContrats()

    try:
        if form_update.validate_on_submit():
            id_artiste_update = form_update.id_artiste_update_wtf.data
            date_contrat_update = form_update.date_contrat_update_wtf.data
            description_contrat_update = form_update.description_contrat_update_wtf.data
            montant_update = form_update.montant_update_wtf.data

            valeur_update_dictionnaire = {
                "value_id_contrat": id_contrat_update,
                "value_id_artiste": id_artiste_update,
                "value_date_contrat": date_contrat_update,
                "value_description_contrat": description_contrat_update,
                "value_montant": montant_update
            }

            str_sql_update_contrat = """UPDATE t_contrats SET 
                                        ID_Artiste = %(value_id_artiste)s, 
                                        Date_Contrat = %(value_date_contrat)s, 
                                        Description_Contrat = %(value_description_contrat)s,
                                        Montant = %(value_montant)s 
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

            form_update.id_artiste_update_wtf.data = data_contrat["ID_Artiste"]
            form_update.date_contrat_update_wtf.data = data_contrat["Date_Contrat"]
            form_update.description_contrat_update_wtf.data = data_contrat["Description_Contrat"]
            form_update.montant_update_wtf.data = data_contrat["Montant"]

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

                form_delete.id_artiste_delete_wtf.data = data_contrat["ID_Artiste"]
                form_delete.date_contrat_delete_wtf.data = data_contrat["Date_Contrat"]
                form_delete.description_contrat_delete_wtf.data = data_contrat["Description_Contrat"]
                form_delete.montant_delete_wtf.data = data_contrat["Montant"]

            btn_submit_del = False

    except Exception as e:
        raise ExceptionContratDeleteWtf(f"fichier : {Path(__file__).name}  ;  {gestion_contrats_delete_wtf.__name__} ; {e}")

    return render_template("contrats/contrat_delete_wtf.html", form_delete=form_delete, btn_submit_del=btn_submit_del, data_contrats_associes=data_contrats_attribue_contrat_delete)
