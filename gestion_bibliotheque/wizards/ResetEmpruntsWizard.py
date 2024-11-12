# wizards/reset_emprunts_wizard.py
from odoo import models, fields, api
from odoo.exceptions import UserError


class ResetEmpruntsWizard(models.TransientModel):
    _name = 'bibliotheque.reset.emprunts.wizard'
    _description = 'Reset Borrower Loans Wizard'

    emprunteur_id = fields.Many2one('bibliotheque.emprunteur', string='Borrower', required=True)
    nb_emprunts = fields.Integer(string='Number of loans to delete', compute='_compute_nb_emprunts')
    confirmation = fields.Boolean(string='I confirm that I want to delete all loans')

    @api.depends('emprunteur_id')
    def _compute_nb_emprunts(self):
        for wizard in self:
            wizard.nb_emprunts = len(wizard.emprunteur_id.emprunt_ids)

    def action_reset_emprunts(self):
        self.ensure_one()
        if not self.emprunteur_id.emprunt_ids:
            raise UserError("This borrower has no loans to delete.")

        # Delete all loans
        self.emprunteur_id.emprunt_ids.unlink()

        # Show notification and close wizard
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Success',
                'message': 'All loans have been deleted successfully',
                'type': 'success',
                'sticky': False,
                'next': {'type': 'ir.actions.act_window_close'},
            }
        }
