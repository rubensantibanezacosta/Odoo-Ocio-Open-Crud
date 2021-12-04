
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ocio_users(models.Model):
    _inherit = "res.users"
    _name = 'res.users'

    punctuation_avg = fields.Float(string = 'Puntuacion media')
    lastconnection=fields.Datetime(string = 'Ultima conexión')


    #  @api.depends('value')
    #  def _value_pc(self):
    #      for record in self:
    #          record.value2 = float(record.value) / 100

class ocio_events(models.Model):
    _name = 'ocio__open.ocio__open_events'
    _description = 'ocio__open.ocio__open_events'

    
    tittle = fields.Char(string="Titulo")
    date = fields.Datetime(string="Fecha del")
    zone = fields.Char(string="Imagen de Perfil")
    place = fields.Char(string="Rol")
    description = fields.Text(string="Punctuacion media")
    punctuation_avg = fields.Float(string="Punctuacion media")
    organizer = fields.One2many("res.users", "login",string="Organizador" , ondelete="cascade")
    image_id = fields.One2many("ocio__open.ocio__open_images", "url",string="Imagen", null=True , ondelete="cascade")
    createdAt=fields.Date(string="Fecha de registro", auto_now_add=True)
    updatedAt=fields.Date(string="Ultima modificación", auto_now=True)
    lastconnection=fields.Date(string="Ultima conexión")

    #  @api.depends('value')
    #  def _value_pc(self):
    #      for record in self:
    #          record.value2 = float(record.value) / 100

class ocio_images(models.Model):
    _name = 'ocio__open.ocio__open_images'
    _description = 'ocio__open.ocio__open_images'

    
    url = fields.Char(string="Imagen")
    createdAt=fields.Date(string="Fecha de registro", auto_now_add=True)
    updatedAt=fields.Date(string="Ultima modificación", auto_now=True)


    #  @api.depends('value')
    #  def _value_pc(self):
    #      for record in self:
    #          record.value2 = float(record.value) / 100
