#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-6-10 11:49
# @Author  : Michael
# @File    : db.py
# @Software: PyCharm
"""
该模块仅用来测试logging模块功能所用
"""
import logging
from util import logger_gen


logger_gen.setup_logging()
logger = logging.getLogger("my_site")


def connect_db():
    print("db connecting……")
    logger.debug('Doing something')
    logger.info('Info db connected')