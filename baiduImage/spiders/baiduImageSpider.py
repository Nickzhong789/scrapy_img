# -*- coding: utf-8 -*-
import scrapy
import requests
import urllib


from urllib.request import urlretrieve
import os
import re

num = 1

class baiduimageSpider(scrapy.Spider):
    name = 'baiduImage'
    allowed_domain = ["baidu.com"]
    # allowed_domain = ["so.com"]
    start_list = []
    url = 'http://image.so.com/i?src=360pic_strong&z=1&i=0&cmg=b3b683e50e228a19ae0fd6ea11c6a10a&q=%E5%A5%B6%E7%89%9B%E5%9B%BE%E7%89%87%E5%A4%A7%E5%85%A8'
    # url = 'http://image.baidu.com/search/flip?' \
    #       'tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1497491098685_R' \
    #       '&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1497491098685%5E00_1519X735' \
    #       '&word=荷斯坦奶牛'
    start_list.append(url)
    start_urls = start_list


    def parse(self, response):
        path = "E:\\cattle\\"
        if (os.path.exists(path) == False):
            os.mkdir(path)
        pattern_pic = '"objURL":"(.*?)",'
        html = response.body
        html = html.decode('utf-8')
        pic_list = re.findall(pattern_pic, html, re.S) #  获取当前页的原图链接
        global num
        for pic_url in pic_list:
            if pic_url is not None:
                try:
                    filename = str(num) + '.jpg'

                    print(str(path+filename))
                    urlretrieve(pic_url,path +filename)


                except Exception as e:
                    print('下载第%s张图片时失败: %s' % (str(num), str(pic_url)))
                num += 1
                continue


        next_urls = re.findall(re.compile(r'<a href="(.*)" class="n">下一页</a>'), html, flags=0)
        next_url = 'http://image.baidu.com' + next_urls[0] if next_urls else ''
        yield scrapy.Request(response.urljoin(next_url))