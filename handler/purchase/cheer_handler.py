# -*- coding: utf-8 -*-
import urllib2
import traceback
import utils
from utils.code import *
from handler.base.base_handler import BaseHandler, handler
from handler.base.base_handler import BaseHandler
from model.cheer import CheerModel
from utils.exception import ServerError
from model.order import OrderModel
from model.user import UserModel

__author__ = 'guoguangchuan'
__email__ = 'ggc0402@qq.com'


class CheerHandler(BaseHandler):
    @handler
    def post(self):
        union_id = self.get_argument('union_id', '')
        target_union_id = self.get_argument('target_union_id', '')
        cheer_model = self.model_config.first(CheerModel, union_id=union_id, target_union_id=target_union_id)
        if cheer_model:
            raise ServerError(ServerError.NO_REPEAT_CHEER)

        satisfy_cheer_num = int(utils.config.get('global', 'satisfy_cheer_num'))
        cheer_models = self.model_config.all(CheerModel, target_union_id=target_union_id)
        user_model = self.model_config.first(UserModel, union_id=target_union_id)
        order_model = self.model_config.first(OrderModel, user_id=user_model.id, status=4)
        target_cheer_num = len(cheer_models)
        if target_cheer_num >= satisfy_cheer_num:
            raise ServerError(ServerError.CHEER_IS_DONE)
        else:
            if order_model:
                raise ServerError(ServerError.NO_DISCOT_BUY)

        cheer_model = CheerModel(union_id=union_id, target_union_id=target_union_id)
        self.model_config.add(cheer_model)
        target_cheer_num += 1
        target_remain_cheer_num = satisfy_cheer_num - target_cheer_num
        return {'target_remain_cheer_num': target_remain_cheer_num}
