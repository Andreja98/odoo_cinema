from odoo import models, fields, api


# Razlika sto je ovde TransientModel je sto se on ne cuva kao tabela u bazi i brise se nakon nekog vremena
class Wizard(models.TransientModel):
    _name = "cinema.wizard"
    _description = "Cinema wizard model"


    tickets = fields.Integer(string="Number of tickets")
    partner_id = fields.Many2one('res.partner', ondelete='cascade', string="Partner", required=True)
    product_id = fields.Many2one('product.product', string="Product", ondelete='cascade', domain=[('e_ticket', '=', True)])


    # Metoda koja azurira broj prodatih karata preko wizard-a. Dobija se broj prodatih karata za trenutni timetable
    # i uvecava se za broj karata unetih za prodaju preko wizarda.
    def update_sold_seats(self):
        # trenutni_id = self._context.get('active_id')
        # print(trenutni_id)
        self._cr.execute("""Select sold_seats from cinema_timetable where id=%s"""%(self._context.get('active_id')))
        for value in self.env.cr.fetchall():
            self.tickets += value[0]
        self.env['cinema.timetable'].browse(self._context.get('active_ids')).update({'sold_seats': self.tickets})
