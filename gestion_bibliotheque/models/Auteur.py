from email.policy import default

from odoo import models, fields


class Auteur(models.Model):
    _name = 'bibliotheque.auteur'
    _description = 'this is model for the book authers'
    _rec_name = 'nom'

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prenom', required=True)
    date_naissance = fields.Date(string='Date de naissance')
    # default value is algerian
    nationalite = fields.Many2one('res.country', string='Nationalite')
    sexe = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme')
    ])
    livre_ids = fields.One2many('bibliotheque.livre', 'auteur_id', string='Livres')
