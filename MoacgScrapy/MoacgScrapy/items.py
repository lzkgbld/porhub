# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoacgscrapyItem(scrapy.Item):
    # 視頻名稱
     spmc = scrapy.Field()
    #視頻链接
     splj = scrapy.Field()
    #視頻圖片
     sptp = scrapy.Field()
    #視頻類型
     splx = scrapy.Field()
    #視頻時間
     spsj = scrapy.Field()
    #視頻播放圖片
     spbftp = scrapy.Field()
    #視頻播放鏈接
     spbflj = scrapy.Field()
    # 存儲路徑
     spfile = scrapy.Field()
    # 存储数量
     spnum = scrapy.Field()
    # 下载类型
     spdtp = scrapy.Field()