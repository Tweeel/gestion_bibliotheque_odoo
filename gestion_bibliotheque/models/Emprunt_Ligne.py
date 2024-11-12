from odoo import models, fields, api


class Emprunt_ligne(models.Model):
    _name = 'bibliotheque.emprunt_ligne'
    _description = 'bibliotheque.emprunt_ligne'
    _rec_name = 'livre_id'

    isbn = fields.Char(string='ISBN', readonly=True)
    nbre_pages = fields.Integer(string='Nombre de pages', readonly=True)
    langue_livre = fields.Selection([
        ('en', 'anglais'),
        ('fr', 'Francais'),
        ('ar', 'Arabe')
    ], string='Langue', readonly=True)
    # Livre 1 -- 0..n Emprunt_ligne
    livre_id = fields.Many2one('bibliotheque.livre', string='Livre')
    # Empunt 1 -- 0..n Emprunt_ligne
    emprunt_id = fields.Many2one('bibliotheque.emprunt', string='Emprunt')

    @api.onchange('livre_id')
    def _onchange_livre_id(self):
        if self.livre_id:
            self.isbn = self.livre_id.isbn
            self.nbre_pages = self.livre_id.nbre_page
            self.langue_livre = self.livre_id.langue_livre