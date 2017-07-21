# -*- coding: utf-8 -*-
import urllib2
import traceback
from utils.code import *
from handler.base.base_handler import BaseHandler, handler
from handler.base.base_handler import BaseHandler
from model.user import UserModel
from model.address import AddressModel

__author__ = 'guoguangchuan'
__email__ = 'ggc0402@qq.com'


class SignupHandler(BaseHandler):
    @handler
    def get(self):
        name = self.get_argument('name')
        phone = self.get_argument('phone')
        address = self.get_argument('address')
        user_model = self.model_config.first(UserModel, union_id=self.session.get('union_id'))  # type:UserModel
        user_model.name = name
        user_model.phone = phone
        user_model.address = address
        self.model_config.commit()
        self.set_header('Content-type', 'text/html')
        self.render('purchase/pay.html', name=name, phone=phone, address=address, price=1)
        res = {
            'render': True
        }
        return res

    @handler
    def post(self):
        name = self.get_argument('name')
        phone = self.get_argument('phone')
        address = self.get_argument('address')
        user_model = self.model_config.first(UserModel, union_id=self.session.get('union_id'))  # type:UserModel
        user_model.name = name
        user_model.phone = phone
        user_model.address = address
        res = {
            'name': name,
            'phone': phone,
            'address': address,
            'price': 1
        }
        return res
