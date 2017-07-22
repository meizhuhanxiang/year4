#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
基础异常类, 为了更好的管理客户端异常状态, 客户端禁止抛出其他异常
"""
__author__ = 'guoguangchuan'


class BaseError(Exception):
    BASE_CODE = 0
    message_zh = ''

    def __init__(self, status, **kwargs):
        self.status_code = int(status[0])
        try:
            self.message = status[1].format(**kwargs)
            self.message_zh = status[2].format(**kwargs)
        except KeyError, e:
            raise Exception('Arg missing for exception: %s' % e)

    def split(self):
        return self.status_code + self.BASE_CODE, '{msg}'.format(msg=(self.message_zh or self.message))

    def __repr__(self):
        return u'StatusCode: %s, Message: %s' % (self.BASE_CODE + self.status_code, self.message)

    def __str__(self):
        return self.__repr__()


class LocalServerError(BaseError):
    BASE_CODE = 50000
    ARGS_MISSING = (1, '{args} are required.', '缺少参数{args}')


class DatabaseError(BaseError):
    BASE_CODE = 10000
    DATABASE_COMMIT_ERROR = (1, 'Database commit error:{args}', '提交数据库发生错误, 已回滚请重试, 错误信息:{args}')


class NetworkError(BaseError):
    BASE_CODE = 20000


class ServerError(BaseError):
    BASE_CODE = 30000
    ARGS_MISSING = (1, '{args} are required.', '缺少参数{args}')
    NO_REPEAT_BUY = (2, 'only on tickit', '对不起，一个用户只能购买一张票')
    NO_REPEAT_CHEER = (3, 'only on tickit', '您已经加过油, 不能重复加油')
    CHEER_IS_DONE = (4, 'only on tickit', '您的好友已经集赞完成，非常感谢')


class SyncError(BaseError):
    BASE_CODE = 40000
    ARG_MISSING = (1, 'only on tickit', '对不起，一个用户只能购买一张票')


if __name__ == '__main__':
    raise SyncError(SyncError.UPDATE_IS_STARTING)
