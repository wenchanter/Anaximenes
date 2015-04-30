# -*- coding: utf-8 -*-

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.news

class DocService:
  
  def __init__(self, topicid):
    self.topicid = 'T%s' % topicid
    self.docs = db.docs[self.topicid]


  def saveDoc(self, doc):
    self.docs.insert_one(doc)

  def getDocs(self):
    return self.docs.find()


if __name__ == '__main__':
  service = DocService('003402E6')
  docs = service.getDocs()
  for doc in docs:
    print doc
