# -*- coding: utf-8 -*-

import logging

class NewsLogger:
  
  def __init__(self, path, name, level=logging.DEBUG):
    self.path = path
    self.level = level
    self.name = name

  def initlogger(self):
    logger = logging.getLogger(self.name)
    logger.setLevel(self.level)
    
    fh = logging.FileHandler(self.path)
    fh.setLevel(self.level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')
    fh.setFormatter(formatter)

    logger.addHandler(fh)

    return logger

  def getLogger(self):
    logger = self.initlogger()
    return logger


if __name__ == '__main__':
  log = NewsLogger('/home/tmp/log/pylogtest.log')
  logger = log.getLogger()
  logger.info('log test')

