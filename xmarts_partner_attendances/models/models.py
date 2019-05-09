# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date, time, timedelta
from odoo.http import request


class PartnerAttendance(models.Model):
    _name = "res.partner.attendance"
    _description = "Partner Attendance"

    name = fields.Char(string='Visitante', required=True, copy=False, readonly=True, default='New')
    state = fields.Selection([('inside', 'Entrada'), ('outside', 'Salida')], default='inside')
    partner_id = fields.Many2one('res.partner', string="Visitante", required=True, ondelete='cascade', index=True)
    check_in = fields.Datetime(string="Ingreso", default=fields.Datetime.now, required=True)
    location_in = fields.Char(string='En: ', default=lambda self: self.env.user.street, readonly=True, store=True)
    location_outt = fields.Char(string='En: ', compute='location_out', readonly=True, store=True)
    check_out = fields.Datetime(string="Salida")
    employee_id = fields.Many2one("hr.employee", string="¿A quien visita?")
    photo_partner = fields.Binary(string="Foto Contacto")
    photo_equipment = fields.Binary(string="Foto Equipo")
    provider_id = fields.Many2one("res.partner", related="partner_id.parent_id", string="Empresa")
    subject = fields.Char(string="Asunto")
    ticket_number = fields.Char(string="No. Gafete", required=True)
    id_photo = fields.Binary(string="Identificacion")
    placas = fields.Binary(string='Matricula')
    comentario = fields.Text(string='Comentarios')

    @api.model
    def create(self, vals):
        cr = self.env.cr
        cr.execute('select coalesce(max(id), 0) from "res_partner_attendance"')
        id_returned = cr.fetchone()
        if (max(id_returned) + 1) < 10:
            vals['name'] = "Reg00" + str(max(id_returned) + 1)
        if (max(id_returned) + 1) >= 10 and (max(id_returned) + 1) < 100:
            vals['name'] = "Reg0" + str(max(id_returned) + 1)
        if (max(id_returned) + 1) >= 100:
            vals['name'] = "Reg" + str(max(id_returned) + 1)
        result = super(PartnerAttendance, self).create(vals)
        return result

    @api.multi
    def check_out_r(self):
        self.check_out = datetime.now()
        self.state = 'outside'

    @api.one
    @api.depends('check_out', 'location_outt')
    def location_out(self):
        if self.check_out:
            self.location_outt = self.env.user.street


class InheritAttendance(models.Model):
    _inherit = 'hr.attendance'

    location_in = fields.Char(string='En: ', default=lambda self: request.env.user.street)
    location_outt = fields.Char(string='En: ', compute='_location_out', store=True)

    @api.one
    @api.depends('check_out', 'location_outt')
    def _location_out(self):
        if self.check_out:
            self.location_outt = str(request.env.user.street)

    # @api.one
    # def _get_current_login_user(self):
    #     user_obj = self.env['res.users'].search([])
    #     for user_login in user_obj:
    #         current_login= self.env.user
    #         if user_login == current_login:
    #             self.location_outt = current_login.name

    #     return
