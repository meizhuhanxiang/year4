# -*- coding: utf-8 -*-
import urllib2
import traceback
from utils.code import *
from handler.base.base_handler import BaseHandler, handler
from handler.base.base_handler import BaseHandler
from model.cheer import CheerModel
import utils

__author__ = 'guoguangchuan'
__email__ = 'ggc0402@qq.com'


class ActivityHandler(BaseHandler):
    @handler
    def get(self):
        self.set_header('Content-type', 'text/html')
        status = int(utils.config.get('global', 'finish'))
        self.render('purchase/activity.html', status=status)
        res = {
            'render': True
        }
        return res
