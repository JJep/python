# -*- coding: utf-8 -*-
import scrapy


class ScrapydocSpider(scrapy.Spider):
    name = "ScrapyDoc"
    allowed_domains = ["scrapy-chs.readthedocs.org"]
    start_urls = ['http://scrapy-chs.readthedocs.org/zh_CN/latest']

    def parse(self, response):
        if response.url.split("/")[-1] == '':
        	filename = response.url.split("/")[-2]
        else:
        	dirname = response.url.split("/")[-2]
        	#判断是否有此目录，如果没有就新建
        	if os.path.isdirname == False:
        		os.mkdir(dirname)
        	filename = '/'.join(response.url.split("/")[-2:])

        #保存文件
        open(filename,'wb').write(response.body)

        sel = HtmlXXpathSelector(response)
        sites = sel.select('//li[@class="toctree-|1"]')
        for site in sites:
        	item = ScrapydocItem()
        	item['title'] = site.select('a/text()').extract()

        	#生成连接begin， 因为从页面提取的连接都是相对地址
        	link = site.select('a/@href').extract()[0]
        	url = response.url

        	#地址形式是否为../spiders.html 这种形式，需要回到上级地址
        	if link.split('/')[0] == '..':
        		url2 = '/'.join(url.split('/')[0:-2]) + '/' + '/'.join(link.split('/')[1:])
        	else:
        		url2 = '/'.join(url.split('/')[0:-1]) + '/' + link

       		item['link'] = [url2]
       		#生成连接end
       		yield item

       		#返回多个request
       		yield Request(url=url2, callback = self.parse)

       	return
