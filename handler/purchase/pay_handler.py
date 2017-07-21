#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from handler.base.base_handler import BaseHandler, handler
import uuid
from model import OrderModel
from model import AddressModel
from model import CommodityModel
from model import OptionModel
from model import AttributeModel
from model import UserModel
from model.cheer import CheerModel
import utils.config
from utils.exception import *
from wechatpy.pay import WeChatPay
from wechatpy.pay.api import WeChatOrder
from utils.exception import ServerError


class PayHandler(BaseHandler):
    @handler
    def post(self):
        out_trade_no = str(uuid.uuid1()).replace('-', '')
        user_model = self.model_config.first(UserModel, union_id=self.session.get('union_id'))  # type:UserModel
        order_model = self.model_config.first(OrderModel, user_id=user_model.id,
                                              status=OrderModel.STATUS_WAIT_SEND)  # type: OrderModel
        if order_model:
            raise Exception('对不起，一个用户只能购买一张票')
        order_model = OrderModel(user_id=user_model.id, status=OrderModel.STATUS_WAIT_PAY, out_trade_no=out_trade_no)
        satisfy_cheer_num = int(utils.config.get('global', 'satisfy_cheer_num'))
        cheer_models = self.model_config.all(CheerModel, target_union_id=user_model.union_id)
        price = 0.02
        if len(cheer_models) >= satisfy_cheer_num:
            price = 0.01
        desc = '宇珩科技有限公司街舞社四周年庆门票预售'
        body = u'棒棒预售-%s' % desc
        web_url = utils.config.get('global', 'url')
        wechat_conf = utils.config.get_section('wechat')
        app_id = wechat_conf['appid']
        key = wechat_conf['key']
        mchid = wechat_conf['mchid']
        mch_cert = wechat_conf['mch_cert']
        mch_key = wechat_conf['mch_key']
        wechat_client = WeChatPay(app_id, key, mchid, mch_cert=mch_cert, mch_key=mch_key)  # type:WeChatOrder
        wechat_order_client = wechat_client.order
        uni_res = wechat_order_client.create('JSAPI', body, int(price * 100),
                                             '%s/api/purchase/notify' % web_url,
                                             user_id=self.session['open_id'], out_trade_no=out_trade_no)
        wechat_jsapi_client = wechat_client.jsapi
        appapi_params = wechat_jsapi_client.get_jsapi_params(uni_res['prepay_id'])
        res = {
            'appapi_params': appapi_params,
            'out_trade_no': out_trade_no
        }
        self.model_config.add(order_model)
        return res
