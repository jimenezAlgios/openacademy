# -*- coding: utf-8 -*-

from openerp import models,fields


class Student (models.Model):
   
    _inherit = 'res.partner'
      
    #El att name de res.partner le decimos que sea requerido puesto que por defecto en res.partner no esta    
    name = fields.Char(required=True)
    
    # Se crea un campo que se llama tipoestudiante, es un desplegable que es de tipo selection
    tipoestudiante = fields.Selection()
    
    # se crea checkbox a false
    student = fields.Boolean("Student", default=False)
    
    #Se pone un campo descripcion ( mirar si res.partne ya tiene uno, si lo tiene se quita)
    description = fields.Text()   
        