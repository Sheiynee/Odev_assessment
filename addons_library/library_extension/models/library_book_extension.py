from odoo import models, fields, api

class LibraryExtension(models.Model):
    _inherit = "library.book"

    author_id = fields.Many2one('res.partner', string='Author', required=True)
    category_id = fields.Many2many('library.book.category', string='Category', widget='many2many_tags')