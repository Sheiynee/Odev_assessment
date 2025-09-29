from odoo import models, fields, api

class LibraryCategory(models.Model):  
    _name = "library.book.category"   
    _description = "Library Book Category"
    _order = "name asc"
    
    name = fields.Char('Category Name', required=True)
    
    _sql_constraints = [
        ('unique_category_name', 'UNIQUE(name)', 'The Category name already exists!')
    ]