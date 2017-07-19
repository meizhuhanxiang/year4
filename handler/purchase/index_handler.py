# -*- coding: utf-8 -*-
import urllib2
import traceback
from utils.code import *
from handler.base.base_handler import BaseHandler, handler
from handler.base.base_handler import BaseHandler
from model.cheer import CheerModel

__author__ = 'guoguangchuan'
__email__ = 'ggc0402@qq.com'


class IndexHandler(BaseHandler):
    @handler
    def get(self):

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
            if cheer_num > 20:
                cheer_num = 20
            remain_cheer_num = 20 - cheer_num
            self.session['target_union_id'] = ''
            self.set_header('Content-type', 'text/html')
            self.render('purchase/cheer.html', union_id=union_id, target_union_id=target_union_id,
                        remain_cheer_num=remain_cheer_num, satisfy_cheer_num=20)
        else:
            cheer_models = self.model_config.all(CheerModel, target_union_id=union_id)
            cheer_num = len(cheer_models)
            self.logger.info('*****************%s' % cheer_num)
            if cheer_num > 20:
                cheer_num = 20
            remain_cheer_num = 20 - cheer_num
            self.set_header('Content-type', 'text/html')
            self.render('purchase/index.html', union_id=union_id, remain_cheer_num=remain_cheer_num,
                        satisfy_cheer_num=20)

        res = {
            'render': True
        }
        return res
