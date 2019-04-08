# -*- coding:UTF-8 -*-

import logging
import os
import time

"""
指定保存日志的文件路径，日志级别，以及调用文件
将日志存入到指定的文件中
:param logger:
"""


class Logger(object):
    # 创建一个Logging类
    logger2 = logging.getLogger('AUTOTEST')

    @classmethod
    def __init__(cls):
        # 判断文件夹是否存在
        if not os.path.exists('../log/'):
            os.makedirs('../log')
        # 设置log等级
        cls.logger2.setLevel(logging.DEBUG)
        # 创建一个handler 写入文件
        rq = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        # 设置编码格式
        fh = logging.FileHandler('../log/{0}.log'.format(rq), encoding='utf-8')
        # 在创建一个handler 打印到控制台
        ch = logging.StreamHandler()
        # 定义handler输入格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logging添加handler
        cls.logger2.addHandler(fh)
        cls.logger2.addHandler(ch)

    # 方法为日志输出
    def log(self, something):
        self.logger2.info(something)
# Logger().log(123)
