from odoo import models, fields, api


class Emprunteur(models.Model):
    _name = 'bibliotheque.emprunteur'
    _description = 'bibliotheque.emprunteur'

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prenom', required=True)
    date_naissance = fields.Date(string='Date de naissance')
    # default value is algerian
    state = fields.Char(string='Nationalite', default='algérienne')
    sexe = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme')
    ])
