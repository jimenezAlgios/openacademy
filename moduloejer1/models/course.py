# -*- coding: utf-8 -*-

from openerp import models, fields

class Course (models.Model):
    
    _inherit = 'openacademy.course'
    
    category_id = fields.Many2one('openacademy.course.category', string="Category")
    