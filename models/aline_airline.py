from odoo import models, fields     
class Airline(models.Model): 
    _name = 'aline_db.airline' 
    name = fields.Char('Name', required=True) 
    #country_id = fields.Many2One('Country', required=True)
    iata_member = fields.Boolean('IATA Membership')
    #ialliance = fields.Many2One('Alliance')

