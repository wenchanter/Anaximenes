# -*- coding: utf-8 -*-

from mustaine.client import HessianProxy
import urllib2
import json

proxy = HessianProxy('http://webservice.build.index.com:9011/webservice/3gcms')

class TopicFetcher:

  def getAllTopic(self, offset, size):
    return proxy.getAllTopicids(offset, size)
    

if __name__ == '__main__':
  tf = TopicFetcher()
  topics =  tf.getAllTopic(0, 10);
  print type(str(topics[0]))

