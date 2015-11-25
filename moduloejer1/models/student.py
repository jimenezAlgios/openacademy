# -*- coding: utf-8 -*-

from openerp import models,fields


class Student (models.Model):
   
    _inherit = 'res.partner'
      
    #El att name de res.partner le decimos que sea requerido puesto que por defecto en res.partner no esta    
    name = fields.Char(required=True)
    
    # Se crea un campo que se llama tipoestudiante, es un desplegable que es de tipo selection--> se crea una columna nueva en la BD de estudiante
    tipoestudiante = fields.Selection([('A','tipoA'),('B','TipoB'),('C','TipoC')], string='Tipo', required=True) 
       
    #fields.Selection([('open', 'New'), ('confirm', 'Validated')], string='Status', required=True, readonly=True, copy=False, default='open')  
    
    # se crea checkbox a false
    student = fields.Boolean("Student", default=False)
    
    #Se pone un campo descripcion ( mirar si res.partne ya tiene uno, si lo tiene se quita)
    #description = fields.Text()   
                  
    #un estudiante puede tener solo un tipo  A, B o C
    #tipoestudiante_id = fields.Many2one('openacademy.student', string="Student")
    