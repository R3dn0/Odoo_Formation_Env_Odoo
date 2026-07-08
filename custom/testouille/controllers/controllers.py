# from odoo import http


# class Testouille(http.Controller):
#     @http.route('/testouille/testouille', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testouille/testouille/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('testouille.listing', {
#             'root': '/testouille/testouille',
#             'objects': http.request.env['testouille.testouille'].search([]),
#         })

#     @http.route('/testouille/testouille/objects/<model("testouille.testouille"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testouille.object', {
#             'object': obj
#         })

