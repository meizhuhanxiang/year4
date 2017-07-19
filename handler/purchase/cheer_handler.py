# -*- coding: utf-8 -*-
import urllib2
import traceback
from utils.code import *
from handler.base.base_handler import BaseHandler, handler
from handler.base.base_handler import BaseHandler
from model.cheer import CheerModel

__author__ = 'guoguangchuan'
__email__ = 'ggc0402@qq.com'


class CheerHandler(BaseHandler):
    @handler
    def post(self):
        union_id = self.get_argument('union_id', '')
        target_union_id = self.get_argument('target_union_id', '')
        cheer_model = CheerModel(union_id=union_id, target_union_id=target_union_id)
        self.model_config.add(cheer_model)
        cheer_models = self.model_config.all(CheerModel, target_union_id=target_union_id)
        target_cheer_num = len(cheer_models)
        if target_cheer_num > 20:
            target_cheer_num = 20
        target_remain_cheer_num = 20 - target_cheer_num
        return {'target_remain_cheer_num': target_remain_cheer_num}
