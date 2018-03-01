'''
Created on 2018年3月1日

@author: Halo
'''
# -*- coding: utf-8 -*-
from urllib.request import urlopen, Request
import re
class Spider:
    '''内涵段子爬虫'''
    def loadPage(self,page):
        '''
        @brief定义一个URL请求网页的方法
        @param page 需要请求的第几页
        @return: 返回的页面html
        '''
        url = 'http://www.neihan8.com/article/list_5_' + str(page) + '.html'
        #User-Agent头
        user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'
        
        headers={'User-Agent':user_agent}
        req = Request(url,headers=headers)
        response = urlopen(req)
        html = response.read()
        html=html.decode('GBK')
        
#         找到所有的段子內容<div class="f18 mb20"> </div>
        pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>')
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
    print ('请按下回车开始')
    input()

    #定义一个Spider对象
    mySpider = Spider()
    mySpider.loadPage(1)
    