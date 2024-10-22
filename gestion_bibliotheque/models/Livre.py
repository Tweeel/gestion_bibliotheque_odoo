from odoo import models, fields, api


class Livre(models.Model):
    _name = 'bibliotheque.livre'

    titre = fields.Char(string='Titre', required=True)
    langue_livre = fields.Selection([
        ('en', 'anglais'),
        ('fr', 'Francais'),
        ('ar', 'Arabe')
    ])
    isbn = fields.Char(string='ISBN')
    nbre_page = fields.Char(string='Nombre de Page')
    image_libre = fields.Char(string='Image')
