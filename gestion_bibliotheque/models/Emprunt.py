from odoo import models, fields, api


class Emprunt(models.Model):
    _name = 'bibliotheque.emprunt'

    date_debut = fields.Date(String='Date de Debut', required=True)
    date_fin = fields.Date(String='Date de Fin', required=True)
    rendu = fields.Boolean(string='Rendue')