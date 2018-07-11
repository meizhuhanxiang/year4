#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from handler.base.base_handler import BaseHandler, handler
import uuid
import time
import datetime
from model import ModelConfig
from model import CommodityModel
from model import AttributeModel
from model import UserModel
from model import OrderModel
from model import OptionModel
from model import CourseModel
from utils.exception import ServerError


class SignHandler(BaseHandler):
    @handler
    def post(self):
        name = self.get_argument('name')
        phone = self.get_argument('phone')
        user_model = self.model_config.first(UserModel, union_id=self.session.get('union_id'))  # type:UserModel
        course_model = self.model_config.first(CourseModel, user_id=user_model.id)  # type:UserModel
        if course_model:
            course_model.name = name
            course_model.phone = phone
            self.model_config.commit()
        else:
            course_model = CourseModel(user_id=user_model.id, name=name, phone=phone)
            self.model_config.add(course_model)
        #res = {
        #    ""
        #}
        #return res
    @handler
    def get(self):
        self.set_header('Content-type', 'text/html')
        self.render('course/sign.html')
        res = {
            'render': True
        }
        return res
