from odoo import models, fields     
class Alliance(models.Model): 
    _name = 'aline_db.alliance' 
    name = fields.Char('Name', required=True) 
    website = fields.Char('Website', required=True)
    author_ids = fields.Many2many(
        'res.partner', 
        string='Authors'
    )