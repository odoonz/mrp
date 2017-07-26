# -*- coding: utf-8 -*-
# Copyright 2017 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.tools import float_round


class MrpBom(models.Model):

    _inherit = 'mrp.bom'

    def explode(self, product, quantity, picking_type=False):
        boms_done, orig_lines_done = super(MrpBom, self).explode(
            product, quantity, picking_type=picking_type)
        lines_done = []
        for bom_line, orig_line in orig_lines_done:
            bom_line = bom_line.with_context(product_id=orig_line['product'].id)
            if bom_line.scale_weight:
                qty = (orig_line['product'].weight /
                       bom_line.product_id.weight) * bom_line.product_qty
                rounding = bom_line.product_uom_id.rounding
                orig_line.update(qty=float_round(
                    qty, precision_rounding=rounding, rounding_method='UP'))
            lines_done.append((bom_line, orig_line))
        return boms_done, lines_done
