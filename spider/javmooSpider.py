'''
Created on 2018年3月10日

@author: HL
'''
# -*- coding:utf-8 -*-

import requests
from lxml import etree
import os

class avSpider:
    def __init__(self):
        self.tiebaName = str(input("请输入女优代号（佐々木あき:p8y）:"))
        self.Page = int(input("请输入爬取页码:"))
        self.url = 'https://www.javbus.com/star/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','Accept-Language': 'zh-CN,zh;q=0.8'}
     
    def loadUrl(self):
        pn = str(self.Page)
        #拼凑完整url，获取详细地址目录
        myUrl = self.url + self.tiebaName + '/' + pn
        response  = requests.get(myUrl,headers = self.headers)
        resHtml =response.text
        
        html = etree.HTML(resHtml)
        result = html.xpath('//a[contains(@class,"movie-box")]')
        
        for site in result:
            deUrl = site.xpath('.//@href')[0]
            self.detailUrl(deUrl)
            
    def detailUrl(self,deUrl):
        #获取详细页面内容
        response  = requests.get(deUrl,headers = self.headers)
        resHtml =response.text
        
        html = etree.HTML(resHtml)
        #获取封面图及预览图url
        imgUrl = html.xpath('//a[contains(@class,"bigImage")]/img/@src')[0]
        deImgUrl = html.xpath('//a[contains(@class,"sample-box")]/@href')
        #获取片名
        title = html.xpath('/html/body/div/h3/text()')[0]
        #获取发行日期
        date = html.xpath('/html/body//p[2]/text()')[0]
        #拼凑目录名
        Dir = date + '-' + title
        myDir = Dir.replace('/','-')
        
        #获取影片磁力链接Demo
        magnets = html.xpath('//table[@id="magnet-table"]/tr/td[1]/a[1]/@href')
        print(magnets)
        #调用内容保存方法
        self.savefile(imgUrl,deImgUrl,myDir,magnets)
        
        
        
        
    def savefile(self,imgUrl,deImgUrl,myDir,magnets):
        #保存内容
        print (myDir)
        fullDir = 'H:/test/' + myDir
        while not os.path.exists(fullDir):
            os.mkdir(fullDir)
        os.chdir(fullDir)
        
        #保存封面图  
        images = requests.get(imgUrl,headers = self.headers).content
        with open('./' + myDir +'.jpg', 'wb') as i:
            i.write(images)
            
        #保存预览图
        count = 1
        for url in deImgUrl:
            image = requests.get(url,headers = self.headers).content
            with open('./' + str(count) + '.jpg', 'wb',) as t:
                t.write(image)
            count +=1
            
        #保存磁力链接至txt
        with open('./' + 'magnet.txt', 'a',) as t:
            t.write(str(magnets))
            

# 模拟 main 函数
if __name__ == "__main__":

    # 首先创建爬虫对象
    mySpider = avSpider()
    # 调用爬虫对象的方法，开始工作
    mySpider.loadUrl()