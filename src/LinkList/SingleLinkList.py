'''
Created on 2018年2月28日

@author: Halo
'''
from LinkList.SingleNode import SingleNode

class SingleLinkList(object):
    '''
    单链表
    '''


    def __init__(self):
        '''
                    头部
        '''
        self._head = None 
        
    def is_empty(self):
        '''判断是否为空'''
        return self._head == None
    
    def length(self):
        '''链表长度'''
        count = 0
        cur = self._head
        while cur != None:
            count += 1
            cur = cur.next
        return count
    
    def travel(self):
        '''遍历链表元素'''
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print('')   
        
    def add(self,item):
        '''创建存储节点'''
        Node = SingleNode(item)
        '''添加节点'''
        Node.next = self._head
        self._head = Node
        
    def append(self,item):
        #创建存储节点
        Node = SingleNode(item)
        #判断是否为空
        if self.is_empty():
            self.add(item)
        else:
            #查找尾部
            cur = self._head
            while cur.next != None:
                cur = cur.next
            #添加尾节点
            cur.next = Node
    def insert(self,pos,item):
        #pos小于等于零 加在头部
        if pos <= 0:
            self.add(item)
        #pos大于等于链表长度加在尾部
        elif pos >= self.length():
            self.append(item)
        else:
            #创建存储节点
            Node = SingleNode(item)
            cur = self._head
            while pos>0:
                cur = cur.next
                pos-=1
            Node.next = cur.next
            cur.next = Node
                
            
    def remove(self,item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next
    def search(self,item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
    
if __name__ == "__main__":
    ll = SingleLinkList()
    ll.add(1)
    ll.travel()
    print('-----------')
    ll.add(2)
    ll.travel()
    print('-----------')
    ll.append(3)
    ll.travel()
    print('-----------')
    ll.insert(2, 4)
    ll.travel()
    print('-----------')
    print ("length:",ll.length())
    ll.travel()
    print (ll.search(3))
    print (ll.search(5))
    ll.remove(2)
    print ("length:",ll.length())
    ll.travel()