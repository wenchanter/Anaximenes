# -*- coding: utf-8 -*-

from topic import TopicFetcher
from fetch_doc import FetchDocAndSave
from newslog import NewsLogger
import traceback

class Anaximenes:

  logger = NewsLogger('/home/workspace/python/docspider/log/topic.log', 'topiclog').getLogger()

  def getAllByTopic(self):
    tf = TopicFetcher()
    offset = 0
    size = 20
    topics = tf.getAllTopic(offset, size)
    while topics is not None and len(topics) > 0:
      for topic in topics:
        try:
          Anaximenes.logger.info('topic: %s begin...' % str(topic))
          fs = FetchDocAndSave(str(topic))
          fs.fetchByTopic()
        except Exception, Argument:
          Anaximenes.logger.error('[error] topic: %s error.... %s, ======== %s' % (topic, Argument, traceback.format_exc()))

      offset = offset + size
      topics = tf.getAllTopic(offset, size)


if __name__ == '__main__':
  ser = Anaximenes()
  ser.getAllByTopic()

