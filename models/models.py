# -*- coding: utf-8 -*-

from odoo import models, fields, api


class openacademy(models.Model):
    _name = 'openacademy.course'
    _description = 'OpenAcademy courses'

    name = fields.Char(string="Title", required=True, help="Name of the course")
    description = fields.Text()
