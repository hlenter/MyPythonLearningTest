import urllib.parse
import urllib.request


def loadPage(url, filename):
    print('正在下载'+filename)
    
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    
    request = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(request)
    read = response.read()
    return read


def writeFile(html, filename):
    print("正在存储"+filename)
    with open(filename,'w') as f:
        f.write(str(html))
    print("-"*20)


def tiebaSpider(url, beginPage, endPage):
    """
        负责处理URL,分配每个URL去发送请求
    """
    for page in range(beginPage,endPage+1):
        pn = (page-1)*50
        
        filename = "第"+ str(page) +"页.html"
        fullurl = url + "&pn=" + str(pn)
        html = loadPage(fullurl,filename)
        writeFile(html,filename)
        
if __name__ == '__main__':
    kw = input('請輸入需要爬取的貼吧:')
    beginPage =  int(input("請輸入起始頁:"))
    endPage = int(input("親輸入終止頁:"))
    
    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw":kw})
    
    url = url + key
    tiebaSpider(url,beginPage,endPage)