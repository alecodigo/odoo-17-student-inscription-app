# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class Professor(models.Model):
    _inherit = 'res.partner'

    is_professor = fields.Boolean(string='Is a professor?')
    subject_ids = fields.Many2many('subject', string='Current Subjects')
