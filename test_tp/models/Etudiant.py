from odoo import fields, models, api
from datetime import datetime


class Etudiant(models.Model):
    _name = 'etudiant'
    _description = 'Student Management'

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prenom', required=True)
    date_naissance = fields.Date(string='Date de naissance', required=True)
    age = fields.Integer(string='Age', required=True, compute='_compute_age')
    examen_ids = fields.Many2many('examen', string='Examens')

    @api.depends('date_naissance')
    def _compute_age(self):
        for record in self:
            if record.date_naissance:
                record.age = fields.Date.today().year - record.date_naissance.year
            else:
                record.age = 0