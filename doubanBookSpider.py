# coding = utf-8

import urllib.request
from bs4 import BeautifulSoup
import time

num = 1
start_time = time.time()
#第一页网页网址https://read.douban.com/columns/category/all?sort=hot&start=0
#第二页网页网址https://read.douban.com/columns/category/all?sort=hot&start=10
#第三页网页网址https://read.douban.com/columns/category/all?sort=hot&start=20

url = 'https://read.douban.com/columns/category/all?sort=hot&start='

for i in range(0,1500,10):
	html = urllib.request.urlopen('https://read.douban.com/columns/category/all?sort=hot&start=%d' % i)
	#BeautifulSoup库解析获得的网页，第二个参数一定记住要写上‘lxml’，记住就行
	bsObj = BeautifulSoup(html, 'lxml')

	# print('==============' + '第%d页' %(i/10 + 1) + '==============')
	#  #分析网页发现，每页有10本书，而<h4>标签正好只有10个。
	# h4_node_list = bsObj.find_all('h4') #返回h4标签的list列表
	# for h4_node in h4_node_list:
	#  	#获取h4标签内的a标签，但这里返回是只含1个元素的list
	#  	a_node = h4_node.contents[0]
	#  	title = a_node.contents[0]
	#  	title = '<<' + title + '>>'
	#  	# print('第%d本书' %num, title)
	#  	print(h4_node_list)
	#  	num = num + 1
	# #设置抓数据停顿时间为1秒，防止过于频繁访问该网站
	# time.sleep(1)
	div_node_list = bsObj.find_all('author')
	for div_node in div_node_list:
		print('=============== div_node_list ===============')
		print(div_node)
	time.sleep(0.5)

end_time = time.time()
duration_time = end_time - start_time
print('运行时间总共为%.2f' %duration_time + '秒')
# print('总共抓到%d本书' % num)

