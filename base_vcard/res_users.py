# -*- coding: utf-8 -*-
import uuid
from openerp import models


class User(models.Model):
    _inherit = ['res.users', 'vcard.model']
    _name = 'res.users'
