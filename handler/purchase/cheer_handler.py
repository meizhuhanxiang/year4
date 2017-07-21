# -*- coding: utf-8 -*-
import urllib2
import traceback
import utils
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
        cheer_model = self.model_config.first(CheerModel, union_id=union_id, target_union_id=target_union_id)
        if cheer_model:
            raise Exception('您已经加过油, 不能重复添加')

        satisfy_cheer_num = int(utils.config.get('global', 'satisfy_cheer_num'))
        cheer_models = self.model_config.all(CheerModel, target_union_id=target_union_id)
        target_cheer_num = len(cheer_models)
        if target_cheer_num > satisfy_cheer_num:
            raise Exception('您的好友已经集赞完成，非常感谢')

        cheer_model = CheerModel(union_id=union_id, target_union_id=target_union_id)
        self.model_config.add(cheer_model)
        target_cheer_num += 1
        target_remain_cheer_num = satisfy_cheer_num - target_cheer_num
        return {'target_remain_cheer_num': target_remain_cheer_num}
