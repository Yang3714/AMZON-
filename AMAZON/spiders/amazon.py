# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
from AMAZON.items import AmazonItem
# from scrapy.http import Request
# from scrapy.spiders import Spider,CrawlSpider,XMLFeedSpider,CSVFeedSpider,SitemapSpider
# from scrapy.selector import HtmlXPathSelector #response.xpath

# print(Spider is scrapy.Spider)
# print(XMLFeedSpider is scrapy.XMLFeedSpider)
# print(Request is scrapy.Request)

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.cn']
    start_urls = ['http://www.amazon.cn/',]

    custom_settings = {
        "BOT_NAME" : 'EGON_AMAZON',                     #可以通过这样方式给自己的爬虫程序加上请求头
        'REQUSET_HEADERS':{},
    }

    def __init__(self,keyword,*args,**kwargs):
        super(AmazonSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword
    def start_requests(self):
        url='https://www.amazon.cn/s/ref=nb_sb_noss_1/461-4093573-7508641?'
        url+=urlencode({'field-keywords':self.keyword})

        yield scrapy.Request(url,
                             callback=self.parse,
                             dont_filter=True,
                             )
    def parse(self, response):
        # int('%s 解析结果：%s' %(response.url,len(response.body)))

        detail_urls=response.xpath('//*[contains(@id,"result_")]/div/div[3]/div[1]/a/@href').extract()   #取所有
        # print(detail_urls)
        for detail_url in detail_urls:
            yield scrapy.Request(url=detail_url,
                                 callback=self.parse_detail
                                 )
        next_url=response.urljoin(response.xpath('//*[@id="pagnNextLink"]/@href').extract_first())#urljoin可以自动拼接url前面的头信息

        yield scrapy.Request(
            url=next_url,
            callback=self.parse
        )

    def parse_detail(self,response):
        name=response.xpath('//*[@id="productTitle"]/text()').extract_first().strip()
        price=response.xpath('//*[@id="priceblock_saleprice"]/text()').extract_first()
        dis=response.xpath('//*[@id="ddmMerchantMessage"]//text()').extract()
        print(name)
        print(price)
        print(dis)
        item=AmazonItem()
        item["name"]=name
        item["price"]=price
        item['dis']=dis
        return item