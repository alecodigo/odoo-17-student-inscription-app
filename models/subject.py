# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class Subject(models.Model):
    _name = 'subject'
    _description = 'Subject'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description', required=True)
    credits = fields.Integer(string='Credits', required=True)
