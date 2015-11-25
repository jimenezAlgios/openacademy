# -*- coding: utf-8 -*-

from openerp import models, fields

class Course (models.Model):
    #hereda de models que es donde esta course
    _inherit = 'openacademy.course'
    
    category_id = fields.Many2one('openacademy.course.category', string="Category")
    