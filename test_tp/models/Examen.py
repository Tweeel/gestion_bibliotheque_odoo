from email.policy import default

from odoo import models, fields


class Examen(models.Model):
    _name = 'examen'

    num = fields.Integer(string='Numero de la salle')
    date = fields.Date(string='date de exam')
    matiere = fields.Selection([
        ('math', 'math'),
        ('info', 'info'),
        ('chimie', 'chimie'),
        ('physique', 'physique')
    ])
    etudiant_ids = fields.Many2many('etudiant', string='Etudiants')
    nbr_etudiant_examen = fields.Integer(string='Numero etudiant examen')
    salle_id = fields.Many2one('salle', string='Salle')


