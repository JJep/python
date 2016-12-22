# coding=utf-8

import scrapy
import time

class DoubanBookSpider(scrapy.Spider):
	name = 'DoubanBook'
	start_urls = ['https://read.douban.com/columns/category/all?sort=hot&start=']

	# def parse(self, response):
	# 	for href in response.css('.question-summary h3 a::attr(href)'):
	# 		full_url = response.urljoin(href.extract())
	# 		yield scrapy.Request(full_url, callback=self.parse_question)

	# def parse_question(self, response):
	# 	yield {
	# 		'title': response.css('h1 a::text').extract()[0],
	# 		'votes': response.css('.question .vote-count-post::text').extract()[0],
	# 		'body': response.css('.question .post-text').extract()[0],
	# 		'tags': response.css('.question .post-tag::text').extract(),
	# 		'link': response.url,
	# 	}

	
	def parse(self, response):
		for title in response.css('h4 a::text').extract():
			yield {
				'book_name': title
			}
	
	def start_requests(self):
		yield scrapy.Request("https://read.douban.com/columns/category/all?sort=hot&start=",headers = {'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0'}, callback = parse)




	# def parse_ten_books(self, response):
	# 	for i in range(1,10):
	# 		print('book_name: ' + response.css('h4 a::text').extract()[i])
	# 	yield {
	# 		'response': response.css('h4 a::text').extract()[0],
	# 		'text': 'nothing'
	# 	}