# -*- coding: utf-8 -*-

import logging

# 打印在控制台
# logging.warning('Watch out!')
# logging.info('I told you so')

# 记录到文件
logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')