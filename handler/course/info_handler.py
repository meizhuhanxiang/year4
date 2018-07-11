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


class InfoHandler(BaseHandler):
    @handler
    def post(self):
        name = self.get_json_argument('name')
        phone = self.get_json_argument('phone')
        user_model = self.model_config.first(UserModel, union_id=self.session.get('union_id'))  # type:UserModel
        course_model = self.model_config.first(CourseModel, user_id=user_model.id)  # type:UserModel
        res = {"sign": False}
        if course_model:
            res = {"sign": True}
        #res = {
        #    ""
        #}
        return res
