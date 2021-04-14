# Copyright 2020 Calyx Servicios S.A
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, _
from odoo.exceptions import Warning


class PurchaseOrderChannel(models.Model):
    _name = "purchase.order.channel"
    _rec_name = "name"
    _order = "sequence"

    name = fields.Char(string="Channel", ondelete="restrict")
    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=10)

