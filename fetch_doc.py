# -*- coding: utf-8 -*-

from doc import DocService
from fetch import DocFetcher
from topic import TopicFetcher
from newslog import NewsLogger
import datetime
import traceback



class FetchDocAndSave:

  logger = NewsLogger('/home/workspace/python/docspider/log/doc.log', 'doclog').getLogger()

  def __init__(self, topicid):
    self.topicid = topicid
    self.service = DocService(topicid)


  def fetchByTopic(self):
    offset = 0
    size = 100
    docnum = self.fetchByTopicAndSave(offset, size)
    count = docnum
    while docnum > 0:
      try:
        offset = offset + size
        docnum = self.fetchByTopicAndSave(offset, size)
        count = count + docnum
      except Exception, Argument:
        FetchDocAndSave.logger.error('[doc error] topic: %s offset: %d error.... %s, =========== %s' % (self.topicid, offset, Argument, traceback.format_exc()))
    FetchDocAndSave.logger.info('get all doc end: topicid: %s, count: %d' % (self.topicid, count))


  def fetchByTopicAndSave(self, offset, size):
    fetcher = DocFetcher()
    docs = fetcher.getDocByTopic(self.topicid, offset, size)
    for doc in docs:
      doc = self.fixDoc(doc)
      if not self.validateDoc(doc):
        continue
      self.service.saveDoc(doc)
    return len(docs)


  def fixDoc(self, doc):
      doc['ptime'] = datetime.datetime.strptime(doc['ptime'], '%Y-%m-%d %H:%M:%S')
      doc['_id'] = doc['docid']
      del doc['docid']
      del doc['id']
      del doc['daynum']
      return doc


  def validateDoc(self, doc):
    if len(doc['_id']) != 16:
      return False
    if len(doc['body']) < 30:
      return False
    return True


if __name__ == '__main__':
  topicid = '003402E6'
  fs = FetchDocAndSave(topicid)
  fs.fetchByToipcAndSave(0, 2)
#  fetcher = DocFetcher()
#  docs = fetcher.getDocByTopic('003402E6', 0, 1)
#  print fs.fixDoc(docs[0])
#  docs[0]['body'] = 'abcde'
#  print fs.validateDoc(docs[0])
#  docs = fetcher.doFetch(channelid, '2015-04-01 00:00:00', '2015-04-03 00:00:00', 0, 1)


