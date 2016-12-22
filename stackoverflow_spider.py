# coding=utf-8

import scrapy

class StackOverflowSpider(scrapy.Spider):
	name = 'stackoverflow'
	start_urls = ['http://stackoverflow.com/questions?sort=votes']

	def parse(self, response):
		for href in response.css('h3 a::text'):
			# full_url = response.urljoin(href.extract())
			yield {
				'text': href
			}

	# def parse_question(self, response):
	# 	yield {
	# 		'title': response.css('h1 a::text').extract()[0],
	# 		'votes': response.css('.question .vote-count-post::text').extract()[0],
	# 		'body': response.css('.question .post-text').extract()[0],
	# 		'tags': response.css('.question .post-tag::text').extract(),
	# 		'link': response.url,
	# 	}
