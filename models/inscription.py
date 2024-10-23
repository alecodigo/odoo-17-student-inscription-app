# -*- coding: utf-8 -*-


from odoo import api, fields, models, _



class Inscription(models.Model):
    _name = 'student.inscription'
    _description = 'Student Inscription'

    student_id = fields.Many2one('res.partner', string='Student', required=True)
    course_id = fields.Many2one('product.template', string='Course', required=True)
    enrollment_date = fields.Date(string='Enrollment date')
    state = fields.Selection([('waiting', 'Waiting'), ('confirmed', 'Confirmed'), ('cancel', 'Cancel')], string='State', default='waiting')
    

    def action_confirm(self):
        self.state = 'confirmed'
    
    def action_waiting(self):
        self.state = 'waiting'
    
    def action_cancel(self):
        self.state = 'cancel'