'''
Created on 2018年2月26日

@author: Halo
'''
import urllib.parse
import urllib.request


url = "http://www.baidu.com/s"
word = {"wd":"东方红"}
word = urllib.parse.urlencode(word)
newurl =url + "?" + word
headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

request = urllib.request.Request(newurl, headers=headers)

response = urllib.request.urlopen(request)

print(response.read())