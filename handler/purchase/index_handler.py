# -*- coding: utf-8 -*-
import urllib2
import traceback
import utils
from utils.code import *
from handler.base.base_handler import BaseHandler, handler
from handler.base.base_handler import BaseHandler
from model.cheer import CheerModel
from model.order import OrderModel
from model.user import UserModel

__author__ = 'guoguangchuan'
__email__ = 'ggc0402@qq.com'


class IndexHandler(BaseHandler):
    @handler
    def get(self):
        satisfy_cheer_num = int(utils.config.get('global', 'satisfy_cheer_num'))
        pre_tittle = utils.config.get('global', 'pre_tittle')
        self.logger.info('*' * 50)
        union_id = self.session.get('union_id', '')
        target_union_id = self.session.get('target_union_id', '')
        if not target_union_id:
            target_union_id = self.get_argument('union_id', '')
        if not target_union_id:
            return self.redirect('/api/purchase/index?union_id=%s' % union_id)
        if union_id != target_union_id:
            cheer_models = self.model_config.all(CheerModel, target_union_id=target_union_id)
            cheer_num = len(cheer_models)
            if cheer_num > satisfy_cheer_num:
                cheer_num = satisfy_cheer_num
            remain_cheer_num = satisfy_cheer_num - cheer_num
            self.session['target_union_id'] = ''
            self.set_header('Content-type', 'text/html')
            self.render('purchase/cheer.html', union_id=union_id, target_union_id=target_union_id,
                        remain_cheer_num=remain_cheer_num, satisfy_cheer_num=satisfy_cheer_num, pre_tittle=pre_tittle)
        else:
            cheer_models = self.model_config.all(CheerModel, target_union_id=union_id)
            cheer_num = len(cheer_models)
            if cheer_num > satisfy_cheer_num:
                cheer_num = satisfy_cheer_num
            remain_cheer_num = satisfy_cheer_num - cheer_num
            user_model = self.model_config.first(UserModel, union_id=self.session.get('union_id'))
            status = 'cheer_undo'
            if remain_cheer_num <= 0:
                status = 'cheer_done'
            payed_order = self.model_config.first(OrderModel, user_id=user_model.id, status=OrderModel.STATUS_WAIT_SEND)
            if payed_order:
                status = 'cheer_payed'
            self.set_header('Content-type', 'text/html')
            self.render('purchase/index.html', union_id=union_id, remain_cheer_num=remain_cheer_num,
                        satisfy_cheer_num=satisfy_cheer_num, status=status, pre_tittle=pre_tittle)

        res = {
            'render': True
        }
        return res
