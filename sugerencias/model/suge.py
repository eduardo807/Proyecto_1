# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.



from odoo import api, fields, models, _




class sugerecla(models.Model):
    _name = "suge.recla"
    

    name = fields.Char(string='Nombre', required=True, readonly=False,)
   