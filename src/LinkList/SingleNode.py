'''
Created on 2018年2月28日

@author: Halo
'''

class SingleNode(object):
    '''
    单链表的节点
    '''


    def __init__(self, item):
        '''
        item存储数据元素
        '''
        self.item = item
        self.next = None