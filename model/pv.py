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
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import BOOLEAN
from sqlalchemy import text
from sqlalchemy import DateTime
from model.base import *

__author__ = 'guoguangchuan'


class PvModel(Base):
    __tablename__ = 'pv'

    id = Column(Integer, primary_key=True)
    url = Column(String(30), nullable=True, doc="路由")
    union_id = Column(String(30), nullable=True, doc="union_id")
    is_del = Column(BOOLEAN, nullable=False, server_default='0', doc="逻辑删除, true(删除)|false(未删除)")
    update_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    create_time = Column(TIMESTAMP, nullable=False, server_onupdate=text("CURRENT_TIMESTAMP"))
