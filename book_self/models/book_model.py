from odoo import models, fields


class EstateProperty(models.Model):
    _name = 'book.list'
    _description = 'There have mulitple book list'

    name = fields.Char(string="Book Name", required=True)
    description = fields.Text(string="Description")
    price = fields.Float(string="Price", required=True)