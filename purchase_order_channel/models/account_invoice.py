# Copyright 2021 Calyx Servicios S.A
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    channel_id = fields.Many2one(
        "purchase.order.channel", string="Channel", ondelete="restrict"
    ) 

    @api.onchange("origin") 
    def onchange_origin(self):
        order = self.env["purchase.order"].search([("name","=",self.origin)])
        self.channel_id = order.channel_id