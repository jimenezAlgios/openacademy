# -*- coding: utf-8 -*-
{
    'name': "moduloEjer1",

    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'openacademy'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'security/security.xml',
        #'security/ir.model.access.csv',
        #'templates.xml',
        #'views/openacademy.xml'
        ##'views/partner.xml'
        #'views/session_workflow.xml',
        #'views/session_board.xml',
        #'reports.xml'
        'views/instructor.xml',
        'views/category.xml'
        
        
        
        
    ],
 
}