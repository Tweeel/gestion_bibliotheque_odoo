from odoo import models, fields, api
from odoo.fields import Date


class Emprunt(models.Model):
    _name = 'bibliotheque.emprunt'

    date_debut = fields.Date(string='Date de début', required=True, compute='_compute_date_debut')
    date_fin = fields.Date(String='Date de Fin', required=True)
    rendu = fields.Boolean(string='Rendue')
    # Emprunt 0..n -- 1..1 Emprunteur
    emprunteur_id = fields.Many2one('bibliotheque.emprunteur', string='Emprunteur')
    # Emprunt 1 -- 0..n Emprunt_ligne
    emprunt_ligne_ids = fields.One2many('bibliotheque.emprunt_ligne', 'emprunt_id', string='Emprunt Lignes')

    @api.onchange('date_fin')
    def _compute_rendu(self):
        if self.date_fin and self.date_fin < fields.Date.today():
            self.rendu = True
        else:
            self.rendu = False

    @api.depends('date_fin')
    def _compute_date_debut(self):
        for record in self:
            record.date_debut = fields.Date.today()

    @api.constrains('date_debut', 'date_fin')
    def _check_dates(self):
        for record in self:
            if record.date_debut > record.date_fin:
                raise ValueError('La date de début doit être inférieure à la date de fin')
