"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterGenres(FlaskForm):
    nom_evenement_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_evenement_wtf = StringField("Nom événement", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                 Regexp(nom_evenement_regexp,
                                                                        message="Pas de chiffres, de "
                                                                                "caractères "
                                                                                "spéciaux, "
                                                                                "d'espace à double, de double "
                                                                                "apostrophe, de double trait "
                                                                                "union")
                                                                 ])
    date_evenement_wtf = DateField("Date événement", validators=[InputRequired("Date obligatoire"),
                                                                 DataRequired("Date non valide")])
    lieu_wtf = StringField("Lieu", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                               Regexp(nom_evenement_regexp,
                                                      message="Pas de chiffres, de "
                                                              "caractères "
                                                              "spéciaux, "
                                                              "d'espace à double, de double "
                                                              "apostrophe, de double trait "
                                                              "union")
                                               ])

    submit = SubmitField("Enregistrer genre")



class FormWTFUpdateGenre(FlaskForm):
    nom_genre_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_genre_update_wtf = StringField("Clavioter le nom voulu ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(nom_genre_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    date_genre_update_wtf = DateField("Date événement", validators=[DataRequired("Date non valide")], format='%Y-%m-%d')
    lieu_genre_update_wtf = StringField("Lieu", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                            Regexp(nom_genre_update_regexp,
                                                                   message="Pas de chiffres, de "
                                                                           "caractères "
                                                                           "spéciaux, "
                                                                           "d'espace à double, de double "
                                                                           "apostrophe, de double trait "
                                                                           "union")
                                                            ])

    submit = SubmitField("Update table !")



class FormWTFDeleteGenre(FlaskForm):
    """
    Dans le formulaire "genre_delete_wtf.html"

    nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
    submit_btn_del : Bouton d'effacement "DEFINITIF".
    submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
    submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_genre_delete_wtf = StringField("Effacer ce genre", validators=[Length(min=2, max=20, message="min 2 max 20")])
    submit_btn_del = SubmitField("Effacer genre")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")

