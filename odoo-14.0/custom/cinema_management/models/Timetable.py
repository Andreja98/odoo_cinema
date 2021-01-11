from odoo import fields, models, api, exceptions

class Timetable(models.Model):
    _name = "cinema.timetable"
    _description = "Cinema timetable"
    _rec_name = 'room_id'

    date = fields.Datetime(required=True)
    movie_id = fields.Many2one('cinema.movie', ondelete='cascade', string="Movie", required=True)
    premiere = fields.Boolean()
    room_id = fields.Many2one('cinema.room', ondelete='cascade', string="Room")
    total_seats = fields.Integer(compute = "_total")
    sold_seats = fields.Integer()
    remaining_seats = fields.Integer(compute="_remaining")
    # Polje koje je veza ka Room modelu kako bi mogao da dohvatim capacity iz Room-a
    room_capacity = fields.Integer(string="Room capacity", related="room_id.capacity")


    # Daje ukupan broj mesta
    @api.depends('room_capacity')
    def _total(self):
        for record in self:
            record.total_seats = record.room_capacity

    # Proverava da li je ukupan broj mesta veci od broja prodatih mesta. Validaciju radi kada se kreira nov Timetable
    @api.constrains('total_seats', 'sold_seats')
    def _check_seats(self):
        for record in self:
            if record.total_seats < record.sold_seats:
                raise exceptions.ValidationError("Total seats cannot be fewer than sold seats")

    # Daje preostali broj mesta u sali odnosno prazna mesta
    def _remaining(self):
        for record in self:
            record.remaining_seats = record.total_seats - record.sold_seats
