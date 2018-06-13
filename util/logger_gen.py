#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-6-10 13:57
# @Author  : Michael
# @File    : logger_gen.py
# @Software: PyCharm

import os
import logging.config
import yaml

"""
该模块是读取logging_cf.yaml所用
"""


def setup_logging(
        default_path="logging_cf.yaml",
        default_level=logging.INFO,
        env_key='LOG_CFG'
):
    """
    Setup logging configuration
    """
    # path = default_path
    path = os.path.join('util', default_path)
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
