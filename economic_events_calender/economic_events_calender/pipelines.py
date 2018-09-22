# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo

from economic_events_calender.items import EconomicEventsCalenderItem
from economic_events_calender.mongo import cl


class EconomicEventsCalenderPipeline(object):
    def process_item(self, item, spider):
        d = dict(item)
        data = item["data"]
        cl.insert({"data": data})
        return item
