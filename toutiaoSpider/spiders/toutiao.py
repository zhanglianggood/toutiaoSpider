# -*- coding: utf-8 -*-
import json
import re
import requests
import scrapy
import urllib
from bs4 import BeautifulSoup as bs
from urllib import request, parse
from toutiaoSpider.items import ToutiaospiderItem


class ToutiaoSpider(scrapy.Spider):
    name = 'toutiao'
    allowed_domains = ['www.toutiao.com']
    url = "https://www.toutiao.com/api/search/content/?"
    offset = 0
    param = """{
        "offset": "re_offset",
        "format": "json",
        "keyword": "街拍",
        "autoload": "true",
        "count": "20",
        "en_qc": "1",
        "cur_tab": "1",
        "from": "search_tab",
        "pd": "synthesis"
    }"""
    meta = param.replace('re_offset', str(offset))
    # print(meta)
    start_urls = [url + parse.urlencode(json.loads(meta))]
    print(start_urls)

    def parse(self, response):
        data = json.loads(response.body)
        if 'data' in data.keys():
            for each in data.get('data'):
                if 'title' in each.keys() and 'id' in each.keys():
                    title = each.get('title')
                    id = each.get('id')
                    image_url = "http://www.toutiao.com/a" + id
                    # print(title)
                    # print(image_url)
                    if image_url:
                        yield scrapy.Request(image_url, callback=self.parse_page_detail,
                                             meta={"title": title, "image_url": image_url})
        self.offset += 20
        if self.offset < 20:
            meta_p = self.param.replace('re_offset', str(self.offset))
            yield scrapy.Request(self.url + parse.urlencode(json.loads(meta_p)), callback=self.parse)

    def parse_page_detail(self, response, ):
        item = ToutiaospiderItem()
        data = response.body
        res_1 = re.compile('img src&#x3D;&quot;(.*?)&quot; img_width', re.S)
        res_2 = re.compile('title: \'(.*?)\',.*?gallery: JSON\.parse\("(.*?)"\)', re.S)
        base_data_1 = re.findall(res_1, data.decode("utf-8"))
        base_data_2 = re.findall(res_2, data.decode("utf-8"))
        item["title"] = response.meta.get("title")
        item["image_url"] = response.meta.get("image_url")

        # print(response.meta.get("title"))
        # print(response.meta.get("page_url"))
        if base_data_1:
            images_url = base_data_1
        elif base_data_2:
            # print(base_data_2)
            base_data_2 = json.loads(base_data_2[0][1].replace('\\', ''))
            images_url = [each_url.get("url") for each_url in base_data_2.get("sub_images")]
            # print(images_url)
        else:
            images_url = ["not data"]
        item["images_url"] = images_url
        yield item
