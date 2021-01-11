from odoo import fields, models

class Room(models.Model):
    _name = "cinema.room"
    _description = "Cinema room"

    timetable_ids = fields.One2many('cinema.timetable', 'room_id', string="Timetable")
    capacity = fields.Integer(string="Room capacity", required=True)
