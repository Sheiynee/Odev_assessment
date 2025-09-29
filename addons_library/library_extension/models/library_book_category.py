from odoo import models, fields, api

class LibraryCategory(models.Model):
    __name__ = "library.book.category"
    _description = "Library Book Category"
    _order = "name asc"
    
    name = fields.Char('Category Name', required=True, compute='_compute_unique_name', store=True)

    @api.depends('name')
    def _compute_unique_name(self):
        for record in self:
            record.name = record.name
