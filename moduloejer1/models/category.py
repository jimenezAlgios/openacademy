# -*- coding: utf-8 -*-
from openerp import models, fields


class Category (models.Model):
    _name= 'openacademy.course.category'
    #Hacer que los campos sean obligatorios con required
    code = fields.Char(required=True)
    name = fields.Char(required=True)
    description = fields.Text()
   # hacer que los campos code y name sean unicos en sql 
   
    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]
    