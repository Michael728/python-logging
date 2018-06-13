#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-6-10 11:47
# @Author  : Michael
# @File    : app.py
# @Software: PyCharm

import logging
from mysite import db
from util import logger_gen
from util import git_helper

logger_gen.setup_logging()
logger = logging.getLogger('app')


def main():
    logger.info('Started')
    git_helper.git_clone()
    db.connect_db()
    logger.info('Finished')


if __name__ == '__main__':
    main()
    a=10
    b=20
    print(a,b)
