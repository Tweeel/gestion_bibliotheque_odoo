from email.policy import default

from odoo import models, fields, api


class Auteur(models.Model):
    _name = 'bibliotheque.auteur'
    _description = 'this is model for the book authers'

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prenom', required=True)
    date_naissance = fields.Date(string='Date de naissance')
    # default value is algerian
    nationalite = fields.Char(string='Nationalite', default='algérienne')
    sexe = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme')
    ])
