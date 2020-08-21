from odoo import models, fields , api   
class Alliance(models.Model): 
    _name = 'aline_db.alliance' 

    name = fields.Char('Name', required=True) 
    website = fields.Char('Website')
