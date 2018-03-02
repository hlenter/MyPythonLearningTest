'''
Created on 2018年3月1日

@author: Halo
'''
# -*- coding: utf-8 -*-
from urllib.request import urlopen, Request
import re
class Spider(object):
    '''shopping spider'''
    def loadPage(self,page):
        '''
                @brief 定义一个URL请求网页的方法
                @param page 需要请求的第几页
                @return: 返回的页面html
                '''
        url = 'http://www.zdfans.com/page/' + str(page)
        #User-Agent头
        user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'
        
        headers={'User-Agent':user_agent}
        req = Request(url,headers=headers)
        response = urlopen(req)
        html = response.read()
        html=html.decode('utf-8')
        pattern = re.compile(r'target="_blank" title="(.*?)</a>',re.S)
        item_list = pattern.findall(html)

        return item_list
    
    def printOnePage(self, item_list, page):
        """
            @brief 处理得到的段子列表
            @param item_list 得到的段子列表
            @param page 处理第几页
        """

        print ("******* 第 %d 页 爬取完毕...*******" %page)
        for item in item_list:
            print("================")
            print(item)

if __name__ == '__main__':
    """
        ======================
            内涵段子小爬虫
        ======================
    """
    print ('-----------')

    #定义一个Spider对象
    mySpider = Spider()
    it_list = mySpider.loadPage(3)
    mySpider.printOnePage(it_list, 3)
    