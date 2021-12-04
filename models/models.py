
# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
import requests



    
class ocio_users(models.Model):
    _inherit = "res.users"
    _name = 'res.users'

    punctuation_avg = fields.Float(string = 'Puntuacion media')
    lastconnection=fields.Datetime(string = 'Ultima conexión')


    #  @api.depends('value')
    #  def _value_pc(self):
    #      for record in self:
    #          record.value2 = float(record.value) / 100

class ocio__open_ocio__open_events(models.Model):
    _name = 'ocio__open.ocio__open_events'
    _description = 'ocio__open.ocio__open_events'

    
    tittle = fields.Char(string="Titulo")
    date = fields.Datetime(string="Fecha y Hora")
    zone = fields.Char(string="Zona")
    place = fields.Char(string="Rol")
    description = fields.Text(string="Descripción")
    punctuation_avg = fields.Float(string="Puntuacion media")
    organizer = fields.Many2one("res.users", string="Organizador" , ondelete="cascade")
    image_id = fields.Many2one("ocio__open.ocio__open_images", string="Imagen", null=True , ondelete="cascade")
    createdAt=fields.Date(string="Fecha de registro", auto_now_add=True)
    updatedAt=fields.Date(string="Ultima modificación", auto_now=True)


    #  @api.depends('value')
    #  def _value_pc(self):
    #      for record in self:
    #          record.value2 = float(record.value) / 100

class ocio__open_ocio__open_images(models.Model):
    _name = 'ocio__open.ocio__open_images'
    _description = 'ocio__open.ocio__open_images'

    
    url = fields.Char(string="Imagen")
    render = fields.Binary(string='Image', compute='_renderImageFromUrl', store=True, attachment=False)
    createdAt=fields.Date(string="Fecha de registro", auto_now_add=True)
    updatedAt=fields.Date(string="Ultima modificación", auto_now=True)


    @api.depends('url','render')
    def _renderImageFromUrl(self):
        
        for record in self:
            if record.url:
                record.render = base64.b64encode(requests.get(record.url).content)
                
            