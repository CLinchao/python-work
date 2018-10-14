#爬取Y站的图片
import os
import urllib.request
import requests
from bs4 import BeautifulSoup
def get_url(url):#获取链接
	req = requests.get(url=url)
	html = req.text
	return html
def get_picture(url):#获取每张图片的链接并且储存至列表
	html = get_url(url)
	bf = BeautifulSoup(html,features='lxml')
	images = bf.find_all('img',class_='preview')
	srcs = [each.get('src') for each in images]
	return srcs
def main(month,folder='E://pachong',load_num=1):#month 为爬取的月份
	month = int(month)
	if not os.path.exists(folder):
		os.mkdir(folder)
	os.chdir(folder)
	while month >= 1:
		url ='https://yande.re/post/popular_by_month?month=%d&year=2018'%month
		pictures_url = get_picture(url)
		for i in pictures_url:
			print("正在爬取第"+str(load_num)+'张图')
			filename = str(load_num) + '.jpg'
			urllib.request.urlretrieve(i,filename)
			print('第'+str(load_num)+'张图爬取完成')
			load_num += 1
		print('第'+str(month)+'月爬取结束')
		month -= 1
if __name__ == '__main__':
	main((input('请输入爬取多少月份:')))
