from odoo import models, fields, api

class Spaceship(models.Model):

    _name = "space.spaceship"
    _description = "Spaceship is faster than a horse"

    dimensions = fields.Char("Ship dimensions")
    fuel_type = fields.Char("Fuel type")
    ship_type = fields.Char("Ship type")
    nr_passengers = fields.Integer("Passengers")
    active = fields.Boolean("Active")
