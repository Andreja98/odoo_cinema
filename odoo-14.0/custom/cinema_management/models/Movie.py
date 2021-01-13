from odoo import fields, models


class Movie(models.Model):
    _name = "cinema.movie"
    _description = "Cinema movies"

    name = fields.Char(string = 'Movie name', required=True)
    genre = fields.Selection([
        ('comedy', 'Comedy'),
        ('action', 'Action'),
        ('animated', 'Animated'),
        ('horor', 'Horor')
    ], default ='comedy', required=True)
    release_year = fields.Integer(string= 'Release year')
    description = fields.Text(string = 'Description')
    image = fields.Binary(string= 'Image')
