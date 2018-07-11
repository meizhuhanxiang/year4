# -*- coding: utf-8 -*-
import urllib2
import traceback
from utils.code import *
from handler.base.base_handler import BaseHandler, handler
from handler.base.base_handler import BaseHandler
from model.cheer import CheerModel
from model.user import UserModel
from model.order import OrderModel
import utils

__author__ = 'guoguangchuan'
__email__ = 'ggc0402@qq.com'


class ActivityHandler(BaseHandler):
    @handler
    def get(self):
        pre_tittle = utils.config.get('global', 'pre_tittle')
        self.set_header('Content-type', 'text/html')
        isfinish = utils.config.get('global', 'isfinish')
        user_model = self.model_config.first(UserModel, union_id=self.session.get('union_id'))
        cheer_models = self.model_config.all(CheerModel, target_union_id=user_model.union_id)
        cheer_num = len(cheer_models)
        satisfy_cheer_num = int(utils.config.get('global', 'satisfy_cheer_num'))
        if cheer_num > satisfy_cheer_num:
            cheer_num = satisfy_cheer_num
        remain_cheer_num = satisfy_cheer_num - cheer_num
        discot = 'null'
        status = 'cheer_undo'
        if remain_cheer_num <= 0:
            status = 'cheer_done'
        payed_order = self.model_config.first(OrderModel, user_id=user_model.id, status=OrderModel.STATUS_WAIT_SEND)
        if payed_order:
            status = 'cheer_payed'
            if remain_cheer_num <= 0:
                discot = 'true'
            else:
                discot = 'false'
        self.render('purchase/activity.html', isfinish=isfinish, status=status, discot=discot, pre_tittle=pre_tittle)
        res = {
            'render': True
        }
        return res
