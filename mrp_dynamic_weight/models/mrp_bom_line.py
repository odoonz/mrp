# -*- coding: utf-8 -*-
# Copyright 2017 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class MrpBomLine(models.Model):

    _inherit = 'mrp.bom.line'

    scale_weight = fields.Boolean(
        string='Scale Weight',
        help='Scale the line quantity by weight of variant',
    )
