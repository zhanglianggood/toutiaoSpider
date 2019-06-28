# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.utils.project import get_project_settings
from toutiaoSpider.settings import MONGODB_HOST, MONGODB_DB, MONGODB_TB
from scrapy.pipelines.images import ImagesPipeline


class ToutiaospiderPipeline(object):
    def __init__(self):
        # client = pymongo.MongoClient(MONGODB_HOST)
        # self.db = client[MONGODB_DB]
        client = pymongo.MongoClient(get_project_settings().get("MONGODB_HOST"))
        self.db = client[get_project_settings().get("MONGODB_DB")]

    def process_item(self, item, spider):
        print(dict(item))
        try:
            # self.db[MONGODB_TB].insert(dict(item))
            self.db[get_project_settings().get("MONGODB_TB")].insert(dict(item))
            print("insert Mongodb Success")
            return True
        except Exception as e:
            print(e)
        # return item
