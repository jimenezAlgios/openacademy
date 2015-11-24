# -*- coding: utf-8 -*-
from openerp import models, fields

class Tipoestudiante (models.Model):
    #sera una opcion de estudiante
    _name= 'openacademy.student.tipo_estudiante'
    
    name = fields.Char(required=True)
    description = fields.Text()
    