# wizards/add_emprunt_wizard.py
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class AddEmpruntWizard(models.TransientModel):
    _name = 'bibliotheque.add.emprunt.wizard'
    _description = 'Add Loans Wizard'

    emprunteur_id = fields.Many2one('bibliotheque.emprunteur', string='Borrower', required=True)
    date_debut = fields.Date(string='Start Date', required=True, default=fields.Date.today)
    date_fin = fields.Date(string='End Date', required=True,
                           default=lambda self: fields.Date.today() + timedelta(days=14))
    line_ids = fields.One2many('bibliotheque.add.emprunt.wizard.line', 'wizard_id',
                               string='Books to Borrow')

    def action_add_emprunts(self):
        self.ensure_one()
        if not self.line_ids:
            raise ValidationError('Please select at least one book to borrow')

        # Create the loan record
        vals = {
            'emprunteur_id': self.emprunteur_id.id,
            'date_debut': self.date_debut,
            'date_fin': self.date_fin,
            'rendu': False,
        }

        # Prepare loan lines
        emprunt_ligne_vals = []
        for line in self.line_ids:
            emprunt_ligne_vals.append((0, 0, {
                'livre_id': line.livre_id.id,
                'isbn': line.livre_id.isbn,
                'nbre_pages': line.livre_id.nbre_page,
                'langue_livre': line.livre_id.langue_livre,
            }))

        vals['emprunt_ligne_ids'] = emprunt_ligne_vals

        # Create the loan
        emprunt = self.env['bibliotheque.emprunt'].create(vals)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'bibliotheque.emprunt',
            'res_id': emprunt.id,
            'view_mode': 'form',
            'target': 'current',
        }


class AddEmpruntWizardLine(models.TransientModel):
    _name = 'bibliotheque.add.emprunt.wizard.line'
    _description = 'Add Loans Wizard Line'

    wizard_id = fields.Many2one('bibliotheque.add.emprunt.wizard', string='Wizard')
    livre_id = fields.Many2one('bibliotheque.livre', string='Book', required=True)
    isbn = fields.Char(related='livre_id.isbn', readonly=True)
    titre = fields.Char(related='livre_id.titre', readonly=True)
    auteur_id = fields.Many2one(related='livre_id.auteur_id', readonly=True)