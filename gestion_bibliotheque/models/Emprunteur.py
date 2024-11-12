from odoo import models, fields, api


class Emprunteur(models.Model):
    _name = 'bibliotheque.emprunteur'
    _description = 'bibliotheque.emprunteur'
    _rec_name = 'nom'

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    date_naissance = fields.Date(string='Date de naissance', required=True)
    # default value is algerian
    state = fields.Char(string='Nationalite', default='algérienne')
    sexe = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme')
    ])
    nbr_emprunt = fields.Integer(string='Nombre d\'emprunts', compute='_compute_nbr_emprunt')

    # Emprunteur 1..1 -- 0..n Emprunt
    emprunt_ids = fields.One2many('bibliotheque.emprunt', 'emprunteur_id', string='Emprunts', required=True)

    @api.depends('emprunt_ids')
    def _compute_nbr_emprunt(self):
        for record in self:
            record.nbr_emprunt = len(record.emprunt_ids)
