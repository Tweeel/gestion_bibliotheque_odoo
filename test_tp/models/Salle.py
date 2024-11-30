from odoo import fields, models


class Salle(models.Model):
    _name = 'salle'
    _rec_name = 'num'

    num = fields.Integer(string='Numero de la salle')
    nbr_etudiant_examen = fields.Integer(string='Numero etudiant examen')
    examen_ids = fields.One2many('examen', 'salle_id', string='Examens')

    nb_examen = fields.Integer(string='Nombre examens')

    def calcule_nbr_math_exam(self):
        count = 0
        for record in self:
            for exam in record.examen_ids:
                if exam.matiere == 'math':
                    count = count + 1
            record.nb_examen = count
            count = 0

    def calcule_students(self):
        for salle in self:
            for exam in salle.examen_ids:
                exam.nbr_etudiant_examen = len(exam.etudiant_ids)
