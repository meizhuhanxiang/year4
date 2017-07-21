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


class IsfinishHandler(BaseHandler):
    def get(self):
        isfinish = int(utils.config.get('global', 'finish'))
        return {'isfinish': isfinish}

    def post(self):
        isfinish = int(utils.config.get('global', 'isfinish'))
        return {'status': isfinish}
