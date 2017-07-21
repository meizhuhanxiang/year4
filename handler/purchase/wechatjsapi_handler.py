# -*- coding: utf-8 -*-
import urllib2
import traceback
import utils
import time
from wechatpy.client import WeChatClient
from wechatpy.client.api import WeChatJSAPI
from utils.code import *
from handler.base.base_handler import BaseHandler, handler
from handler.base.base_handler import BaseHandler
from model.user import UserModel
from model.address import AddressModel
from model.order import OrderModel
from model.user import UserModel

__author__ = 'guoguangchuan'
__email__ = 'ggc0402@qq.com'
NONCESTR = 'Wm3WZYTPz0wzccnW'

class WechatjsapiHandler(BaseHandler):

    @handler
    def post(self):
        current_url = self.get_argument('current_url')
        wechat_conf = utils.config.get_section('wechat')
        app_id = wechat_conf['appid']
        appsecret = wechat_conf['appsecret']
        wechat_client = WeChatClient(app_id, appsecret, self.session.get('access_token'))
        wechat_jsapi = WeChatJSAPI(wechat_client)
        ticket = wechat_jsapi.get_jsapi_ticket()
        timestamps = int(time.time())
        signature = wechat_jsapi.get_jsapi_signature(NONCESTR, ticket, timestamps, current_url)
        res = {
            'appid': app_id,
            'timestamp': timestamps,
            'noncestr': NONCESTR,
            'signature': signature,
            'link': current_url,
            'js_api_list': ['onMenuShareTimeline', 'onMenuShareAppMessage']

        }
        return res
