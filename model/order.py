#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy import TypeDecorator
from sqlalchemy import types
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import TIMESTAMP
from sqlalchemy import Float
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import BOOLEAN
from sqlalchemy import text
from sqlalchemy import DateTime
from model.base import *

__author__ = 'guoguangchuan'


class OrderModel(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, doc="用户id")
    status = Column(Integer, nullable=False, doc="订单状态")
    order_no = Column(String(128), nullable=True, doc="货物订单号")
    out_trade_no = Column(String(128), nullable=True, doc="统一支付订单号")
    cart_time = Column(TIMESTAMP, nullable=True, doc="加入购物车时间")
    price = Column(Float(precision=2), nullable=True, doc="价格")
    pay_time = Column(TIMESTAMP, nullable=True, doc="付款时间")
    is_del = Column(BOOLEAN, nullable=False, server_default='0', doc="逻辑删除, true(删除)|false(未删除)")
    update_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    create_time = Column(TIMESTAMP, nullable=False, server_onupdate=text("CURRENT_TIMESTAMP"))

    STATUS_CART = 1
    STATUS_ORDER_IMMEDIATELY = 2
    STATUS_WAIT_PAY = 3
    STATUS_WAIT_SEND = 4
    STATUS_WAIT_RECEIVE = 5
    STATUS_COMPLETE = 6
    STATUS_CLOSE = 7
    STATUS_ALL = 8

    STATUS_LIST = [STATUS_CART, STATUS_ORDER_IMMEDIATELY, STATUS_WAIT_PAY, STATUS_WAIT_SEND, STATUS_WAIT_RECEIVE,
                   STATUS_COMPLETE, STATUS_CLOSE,
                   STATUS_ALL]
    STATUS_MY_ORDER_LIST = [STATUS_WAIT_PAY, STATUS_WAIT_SEND, STATUS_WAIT_RECEIVE,
                            STATUS_COMPLETE, STATUS_CLOSE,
                            STATUS_ALL]
    STATUS_PAY_LIST = [STATUS_WAIT_SEND, STATUS_WAIT_RECEIVE, STATUS_COMPLETE]
