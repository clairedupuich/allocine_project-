import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from os import write
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import csv


class CrawlAllocineSpider(CrawlSpider):
    name = 'crawl_allocine'
    allowed_domains = ['allocine.fr']
    start_urls = ['http://allocine.fr/'] #???????开始抓取的页面

    rules = (
        # callback='parse_item'是引用下面定义的函数。
        Rule(LinkExtractor(restrict_xpaths ='//a[@class="meta-title-link"]', callback='parse_item', follow=True),
        #定位换页按钮，之后会自动换页。
        Rule(LinkExtractor(restrict_xpaths ="//span[@class='txt']", follow=True), 
    
    )

    def parse_item(self, response):
        item = {}
        #记得在放到这里之前在网页inspeter页面用ctrle+f验证查询结果的数量及相关显示。
        item['name'] = response.xpath('//div[@class ="titlebar-title titlebar-title-lg"]').get()
        item['date'] = response.xpath('//a[@class="xXx date blue-link"]').get()
        item['durée'] = response.xpath('//div[@class="meta-body-item meta-body-info"]/text()[4]').get()
        item['Genre'] = response.xpath('//div[@class="meta-body-item meta-body-info"]/a[@class="xXx"]').get()
        item['Réalisateur'] = response.xpath('//div[@class="meta-body-item meta-body-direction"]/a[@class="xXx blue-link"]').get() #????????2 resulta
        item['Acteurs'] = response.xpath('//div[@class="meta-body-item meta-body-actor"]/a[@class="xXx"]').get()
        item['Synopsis'] = response.xpath('//div[@class="content-txt "]').get()
        
        return item
        
