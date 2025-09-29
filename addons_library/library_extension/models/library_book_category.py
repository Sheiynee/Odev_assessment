from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryCategory(models.Model):
    _name = "library.book.category"
    _description = "Library Book Category"
    _order = "name asc"
    
    name = fields.Char('Category Name', required=True, compute='_compute_unique_name', store=True)

    @api.depends('name')
    def _compute_unique_name(self):
        for record in self:
            if record.name == record.name:
                raise UserError("The Category name is already been used")
