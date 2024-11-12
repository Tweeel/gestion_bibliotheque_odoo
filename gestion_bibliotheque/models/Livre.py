from odoo import models, fields


class Livre(models.Model):
    _name = 'bibliotheque.livre'
    _rec_name = 'titre'

    titre = fields.Char(string='Titre', required=True)
    auteur_id = fields.Many2one('bibliotheque.auteur', string='Auteur')
    langue_livre = fields.Selection([
        ('en', 'anglais'),
        ('fr', 'Francais'),
        ('ar', 'Arabe')
    ], string='Langue')
    isbn = fields.Char(string='ISBN')
    nbre_page = fields.Char(string='Nombre de Page')
    image_libre = fields.Char(string='Image')
    emprunt_ligne_ids = fields.One2many('bibliotheque.emprunt_ligne', 'livre_id', string='Emprunts')
