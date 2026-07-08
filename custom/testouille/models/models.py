# from odoo import models, fields, api


# class testouille(models.Model):
#     _name = 'testouille.testouille'
#     _description = 'testouille.testouille'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

