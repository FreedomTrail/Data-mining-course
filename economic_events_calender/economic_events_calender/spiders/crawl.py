# -*- coding: utf-8 -*-

import scrapy
from economic_events_calender.items import EconomicEventsCalenderItem


class QuotesSpider(scrapy.Spider):
    name = "quots"

    def start_requests(self):
        urls = [
            'https://www.fxstreet.com/economic-calendar'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        price = response.xpath('//*[@id="Content_C163_Col01"]/h2/text()').extract()
        items = EconomicEventsCalenderItem()
        items["data"] = [price]
        return items
