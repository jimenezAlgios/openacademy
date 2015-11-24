# -*- coding: utf-8 -*-

from openerp import models,fields


class Student (models.Model):
    #desde student se podra elegir curso, entiendo que hay que hereedar
        _inherit = 'openacademy.course'
        
        name = fields.Char(required=True)
        description = fields.Text()
        
        
        tipoestudiante_id = fields.Many2one('openacademy.student.tipoestudiante', string="tipoestudiante")
        
        
        