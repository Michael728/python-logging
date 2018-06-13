#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-6-10 20:14
# @Author  : Michael
# @File    : git_helper.py
# @Software: PyCharm

"""
不指定logger名字时，默认使用root的配置，logger名显示为root
指定为__name__时，使用的也是root的配置，logger名为当前模块名，【推荐】
"""

import logging
from util import logger_gen

logger_gen.setup_logging()
logger = logging.getLogger(__name__)


def git_clone():
    logger.info("git clone start")
    try:
        print(1 / 0)
    except ZeroDivisionError as e:
        print(e)
        logger.error('Failed to open file', exc_info=True)  # 将错误打印出来
        # raise
