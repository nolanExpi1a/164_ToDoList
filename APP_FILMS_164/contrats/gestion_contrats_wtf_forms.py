"""
Formulaires avec WTF pour la gestion des contrats.
Fichier : gestion_contrats_wtf_forms.py
Auteur : OM 2021.03.16
"""

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import Length, DataRequired, Regexp


class FormeWTFajouterContrats(FlaskForm):
    """
        Dans le formulaire "contrats_ajouter_wtf.html",
        ID_Contrat, Date_Contrat, et Description_Contrat sont des champs obligatoires.
    """
    id_contrat_wtf = StringField("ID du Contrat", validators=[
        Length(min=2, max=50, message="min 2 max 50"),
        DataRequired(message="Champ obligatoire")
    ])
    id_artiste_wtf = StringField("ID de l'Artiste", validators=[
        Length(min=2, max=50, message="min 2 max 50"),
        DataRequired(message="Champ obligatoire")
    ])
    date_contrat_wtf = DateField("Date du Contrat", format='%Y-%m-%d', validators=[
        DataRequired(message="Champ obligatoire")
    ])
    description_contrat_wtf = StringField("Description du Contrat", validators=[
        Length(min=2, max=50, message="min 2 max 50"),
        DataRequired(message="Champ obligatoire")
    ])
    montant_wtf = StringField("Montant", validators=[
        Length(min=2, max=50, message="min 2 max 50"),
        DataRequired(message="Champ obligatoire")
    ])
    submit = SubmitField("Enregistrer Contrat")


class FormWTFupdateContrats(FlaskForm):
    """
        Dans le formulaire "contrats_update_wtf.html",
        ID_Contrat, Date_Contrat, et Description_Contrat sont des champs obligatoires.
    """
    id_contrat_update_wtf = StringField("ID du Contrat", validators=[
        Length(min=2, max=50, message="min 2 max 50"),
        DataRequired(message="Champ obligatoire")
    ])
    id_artiste_update_wtf = StringField("ID de l'Artiste", validators=[
        Length(min=2, max=50, message="min 2 max 50"),
        DataRequired(message="Champ obligatoire")
    ])
    date_contrat_update_wtf = DateField("Date du Contrat", format='%Y-%m-%d', validators=[
        DataRequired(message="Champ obligatoire")
    ])
    description_contrat_update_wtf = StringField("Description du Contrat", validators=[
        Length(min=2, max=50, message="min 2 max 50"),
        DataRequired(message="Champ obligatoire")
    ])
    montant_update_wtf = StringField("Montant", validators=[
        Length(min=2, max=50, message="min 2 max 50"),
        DataRequired(message="Champ obligatoire")
    ])
    submit = SubmitField("Mettre à jour Contrat")


class FormWTFdeleteContrats(FlaskForm):
    """
        Dans le formulaire "contrats_delete_wtf.html",
        ID_Contrat, Date_Contrat, et Description_Contrat sont des champs obligatoires.
    """
    id_contrat_delete_wtf = StringField("Effacer ce Contrat")
    date_contrat_delete_wtf = DateField("Date du Contrat")
    description_contrat_delete_wtf = StringField("Description du Contrat")
    submit_btn_del = SubmitField("Effacer Contrat")
    submit_btn_conf_del = SubmitField("Etes-vous sûr d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
