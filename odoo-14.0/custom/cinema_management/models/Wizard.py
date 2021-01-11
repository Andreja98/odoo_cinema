from odoo import models, fields, api


# Razlika sto je ovde TransientModel je sto se on ne cuva kao tabela u bazi i brise se nakon nekog vremena
class Wizard(models.TransientModel):
    _name = "cinema.wizard"
    _description = "Cinema wizard model"


    tickets = fields.Integer(string="Number of tickets")
    partner_id = fields.Many2one('res.partner', ondelete='cascade', string="Partner", required=True)
    product_id = fields.Many2one('product.product', string="Product", ondelete='cascade', domain=[('e_ticket', '=', True)])


    # Metoda koja azurira broj prodatih karata preko wizard-a
    def update_sold_seats(self):
        self.env['cinema.timetable'].browse(self._context.get('active_ids')).update({'sold_seats': self.tickets})
