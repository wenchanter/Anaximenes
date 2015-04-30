# -*- coding: utf-8 -*-

from mustaine.client import HessianProxy
import urllib2
import json

proxy = HessianProxy('http://webservice.build.index.com:9011/webservice/3gcms')

class DocFetcher:

  def fetchDoc(self, channelid, ftime, ttime, offset, size):
    return proxy.get3GArticles(channelid, ftime, ttime, offset, size)

  def getDocByTopic(self, topicid, offset, size):
    docs = proxy.getTopicArticle(topicid, offset, size)
    
    for doc in docs:
      print 'id len: %d' % len(doc['docid'])
      doc['body'] = self.getBody(doc['docid'])
      print 'body len: %d, topicid: %s' % (len(doc['body']), doc['topicid'])
    return docs

  def getBody(self, docid):
    url = 'http://c.3g.163.com/nc/article/%s/full.html' % docid
    response = urllib2.urlopen(url)
    docInfo = response.read()
    docJson = json.loads(docInfo)
    if docJson[docid].has_key('body'):
      return docJson[docid]['body'] 
    else:
      return ''

if __name__ == '__main__':
  fetcher = DocFetcher()
#  print fetcher.doFetch('0096', '2015-04-01 00:00:00', '2015-04-03 00:00:00', 0, 1)
  print fetcher.getDocByTopic('003402E6', 1, 2);
#  fetcher.getBody('AM2U46HE00964L1F')
