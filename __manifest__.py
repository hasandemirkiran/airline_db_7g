# -*- coding: utf-8 -*-
{
    'name' : 'Airline Database',
    'version' : '1.0',
    'depends' : ['base'],
    'summary' : 'Transfer Airplane Databases Odoo',
    'author' : "Hasan Demirkiran",
    'website' : "https://www.linkedin.com/in/hasan-demirkıran-ba3798155/",
    'categoty' : "Airline",
    'description': """
    Airplane Database Odoo Modules 
    """,
    #always loaded
    'data': ['views/views.xml'],
    #only load in demonstration mode 
    'demo': ['demo/demo.xml'], 
    'application' : True,
    'auto_install' : False,
    'installable' : True,
}