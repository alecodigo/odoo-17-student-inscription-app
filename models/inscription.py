# -*- coding: utf-8 -*-


from odoo import api, fields, models, _



class Inscription(models.Model):
    _name = 'student.inscription'
    _description = 'Student Inscription'

    name = fields.Char(
        string='Number',
        compute='_compute_name', readonly=False, store=True,
        copy=False,
    )
    student_id = fields.Many2one('res.partner', string='Student', required=True)
    course_id = fields.Many2one('product.template', domain=[('is_course', '=', True)], string='Course', required=True)
    enrollment_date = fields.Date(string='Enrollment date', required=True)
    state = fields.Selection([('waiting', 'Waiting'), ('confirmed', 'Confirmed'), ('cancel', 'Cancel')], string='State', copy=False, default='waiting')
    
    @api.depends('student_id', 'course_id')
    def _compute_name(self):
        for record in self:
            record.name = f"{record.student_id.name} , {record.course_id.name}" 

    def action_confirm(self):
        self.state = 'confirmed'
    
    def action_waiting(self):
        self.state = 'waiting'
    
    def action_cancel(self):
        self.state = 'cancel'