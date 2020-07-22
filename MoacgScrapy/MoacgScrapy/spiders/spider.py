import scrapy
import re, time, os, requests
from MoacgScrapy.items import MoacgscrapyItem
from lxml import etree


class MoacgScrapySpider(scrapy.Spider):
    # 項目名稱
    name = 'MoacgScrapy'
    # 允許範圍
    allowed_domains = ['cn.pornhub.com', 'cn.pornhubpremium.com']
    # 发送请求获取配置信息
    txt_data = []
    # 调用方法将txt数据读取到list中
    for line in open('configure.txt', "r", encoding='UTF-8'):
        txt_data.append(line.strip('\n'))
    # 进行数据分类
    for t in txt_data:
        if t.split("==")[0] in "存储文件夹":
            cl_path = t.split("==")[1]
        elif t.split("==")[0] in "起始页":
            cl_num = t.split("==")[1]
        elif t.split("==")[0] in "结束页":
            cl_end = t.split("==")[1]
        elif t.split("==")[0] in "完整地址":
            cl_url = t.split("==")[1]
        elif t.split("==")[0] in "是否收费(1:免费 2:收费视频)":
            cl_type = t.split("==")[1]
    # 判断数据是否正常
    if len(cl_path) > 0 and len(cl_num) > 0 and len(cl_end) > 0 and len(cl_url) > 0 and len(cl_type) < 0:
        print("错误数据未填写完整")
    if cl_type == "1":
        urls = 'https://cn.pornhub.com'
        cookice = {}
    else:
        urls = 'https://cn.pornhubpremium.com'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
            'Referer': 'https://cn.pornhubpremium.com/premium/login'
        }

        html_login = requests.get('https://cn.pornhubpremium.com/premium/login')
        h_cookie = html_login.cookies
        h_cookie = requests.utils.dict_from_cookiejar(h_cookie)
        html_login = html_login.text
        html = etree.HTML(html_login)
        token = html.xpath('//*[@id="token"]/@value')
        token = token[0]
        redirect = {'from':'pc_premium_login','segment':'straight'}
        # username=用户名  password=密码
        data = {'username': '','password': '','token': token,'redirect':redirect}
        r = requests.post("https://cn.pornhubpremium.com/front/authenticate", headers=headers,data=data,cookies=h_cookie)
        # print(r.text)
        cookice = r.cookies
        cookice = requests.utils.dict_from_cookiejar(cookice)
    start_urls = [
        cl_url + '&page=' + str(cl_num),
    ]

    # 爬虫第一次发送请求带上cookice
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url,cookies=self.cookice,callback=self.parse)

    def parse(self, response):
        items = []
        # 视频连接
        splj = response.xpath('//*[@data-segment="straight"]/div/div[1]/a/@href').extract()
        # 视频名称
        spmc = response.xpath('//*[@data-segment="straight"]/div/div[3]/span/a/@title').extract()
        # 视频图片
        sptp = response.xpath('//*[@data-segment="straight"]/div/div[1]/a/img/@data-src').extract()
        # 视频时间
        spsj = response.xpath('//*[@data-segment="straight"]/div/div[1]/a/div/var/text()').extract()
        for each in range(0, len(spmc)):
            item = MoacgscrapyItem()
            # 視頻鏈接
            item['splj'] = self.urls+splj[each]
            # 視頻名稱
            item['spmc'] = spmc[each]
            #視頻時間
            item['spsj'] = spsj[each]
            items.append(item)
        # 发送每个url的Request请求，得到Response连同包含meta数据 一同交给回调函数 second_parse 方法处理
        for item in items:
            yield scrapy.Request(url=item['splj'], meta={'meta_1': item,'cl_path': self.cl_path}, callback=self.second_parse,cookies=self.cookice)
        # 设置爬取范围
        if self.cl_num < self.cl_end:
            self.cl_num += 1
            yield scrapy.Request(self.cl_url + "&page=" + str(self.cl_num), callback=self.parse,dont_filter=True)

    # 对返回的视频地址url，再进行递归请求
    def second_parse(self, response):
        meta_1 = response.meta['meta_1']
        cl_path = response.meta['cl_path']
        # 視頻類型
        splx = response.xpath('//*[@class="categoriesWrapper"]/a/text()').extract()
        item = MoacgscrapyItem()
        # 視頻類型
        items = []
        for each in range(0,len(splx)):
                items.append(splx[each] + ' ')
        # 视频类型
        item['splx'] = ''.join(items)
        # 视频链接
        item['splj'] = meta_1['splj']
        # 视频名称
        item['spmc'] = meta_1['spmc']
        # 视频时间
        item['spsj'] = meta_1['spsj']
        # 存儲分類文件夾名
        item['spfile'] = cl_path
        # 区分下载类型
        item['spdtp'] = self.cl_type
        yield item