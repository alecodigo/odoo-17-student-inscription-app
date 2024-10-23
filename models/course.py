# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class Curso(models.Model):
    _inherit = 'product.template'

    professor_ids = fields.Many2many('res.partner', string='Profesores', domain=[('is_professor', '=', True)])
    subject_ids = fields.Many2many('subject', string='Subjects')
    date_start = fields.Date(string='Start date')
    duration = fields.Integer(string='Duration (days)')
    max_capacity = fields.Integer(string='maximum capacity')
    is_course = fields.Boolean(string="Is a course?")
