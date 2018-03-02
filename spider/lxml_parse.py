'''
Created on 2018年3月2日

@author: Halo
'''
from lxml import etree
html = etree.parse('./hello.html')
result = etree.tostring(html,pretty_print=True)

print(result)