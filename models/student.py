# -*- coding: utf-8 -*-


from odoo import api, fields, models, _



class Student(models.Model):
    _inherit = 'res.partner'
    
    date_birth = fields.Date(string='Date of birth')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    is_student = fields.Boolean(string='Is student?')


    @api.depends('date_birth')
    def _compute_age(self):
        """ Compute the student age automatically. 
            When the user input the date of birth
        """
        for student in self:
            if student.date_birth:
                today = fields.Date.today()
                student.age = today.year - student.date_birth.year - ((today.month, today.day) < (student.date_birth.month, student.date_birth.day))
            else:
                student.age = 0
