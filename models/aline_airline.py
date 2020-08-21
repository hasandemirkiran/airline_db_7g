from odoo import models, fields, api 
class Airline(models.Model): 
    _name = 'aline_db.airline' 
    name = fields.Char('Name', required=True) 
    airline_id = fields.Many2One('res.partner',string="Airline", required=True)
    country_id = fields.Many2One(string="Country", related="airline_id.country_id" ,readonly=True, store=True)
    iata_member = fields.Boolean(string="IATA Membership")
    alliance = fields.Many2One('aline_db.alliance', string="Alliance")
    service_type = fields.Selection(string="Service Type", selection[('Low Cost'),('Premium Charter'), ('Standart'), ('Domestic'), ('Charter')  ])
    flag_carrier = fields.Boolean(string="Flag Carrier")
    aircraft_no = fields.Integer(string="Number of Aircraft")
    revenue_total = fields.Float(string="Total Revenue")
    revenue_ancillary = fields.Float(string="Ancillary Revenue")

    @api.onchange('airline_id')
    def _country_id_(self):
        self.country_id = self.airline_id.country_id
