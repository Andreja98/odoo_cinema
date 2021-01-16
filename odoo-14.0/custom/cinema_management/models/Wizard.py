from odoo import models, fields, api


# Razlika sto je ovde TransientModel je sto se on ne cuva kao tabela u bazi i brise se nakon nekog vremena
class Wizard(models.TransientModel):
    _name = "cinema.wizard"
    _description = "Cinema wizard model"


    tickets = fields.Integer(string="Number of tickets")
    partner_id = fields.Many2one('res.partner', ondelete='cascade', string="Partner", required=True)
    product_id = fields.Many2one('product.product', string="Product", ondelete='cascade', domain=[('e_ticket', '=', True)])
    account = fields.Many2one('res.users', string="Current user", default=lambda self: self.env.user.id)


    # Metoda koja azurira broj prodatih karata preko wizard-a. Dobija se broj prodatih karata za trenutni timetable
    # i uvecava se za broj karata unetih za prodaju preko wizarda.
    def update_sold_seats(self):
        # trenutni_id = self._context.get('active_id')
        # print(trenutni_id)
        self._cr.execute("""Select sold_seats from cinema_timetable where id=%s"""%(self._context.get('active_id')))
        for value in self.env.cr.fetchall():
            self.tickets += value[0]
        self.env['cinema.timetable'].browse(self._context.get('active_ids')).update({'sold_seats': self.tickets})


    def invoice_creating(self):
        partner = 0
        product = 0
        acc = 0

        for item in self.partner_id:
            partner = int(item)
        for item1 in self.product_id:
            product = int(item1)
        for item2 in self.account:
            acc = int(item2)
        result = self.env['account.move'].create({
            'partner_id': partner,
            'payment_reference': 'payment reference',
            'invoice_date': '2021-01-10',
            'invoice_date_due': '2021-02-10',
            'invoice_payment_term_id': 7})
        result_line = self.env['account.move.line'].create({
                'product_id': product,
                'name': 'Bank fees',
                'quantity': self.tickets,
                'price_unit': 5000,
                'tax_line_id': 1,
                'price_subtotal': 15000,
                'move_id': 1,
                'account_id': acc,
                })


    @api.model
    def create(self, values):
        invoice = super(Wizard, self).create(values)
        return invoice



