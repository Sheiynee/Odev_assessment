from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryCategory(models.Model):
    _name = "library.book.category"
    _description = "Library Book Category"
    _order = "name asc"
    
    name = fields.Char('Category Name', required=True, compute='_compute_unique_name', store=True)

    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            if self.search_count([('name', '=', record.name)]) > 1:
                raise ValidationError("Category name must be unique.")
