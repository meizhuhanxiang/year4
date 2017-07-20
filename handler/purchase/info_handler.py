# -*- coding: utf-8 -*-
import urllib2
import traceback
from utils.code import *
from handler.base.base_handler import BaseHandler, handler
from handler.base.base_handler import BaseHandler
from model.cheer import CheerModel

__author__ = 'guoguangchuan'
__email__ = 'ggc0402@qq.com'


class InfoHandler(BaseHandler):
    @handler
    def get(self):
        self.set_header('Content-type', 'text/html')
        self.render('purchase/info.html')
        res = {
            'render': True
        }
        return res
