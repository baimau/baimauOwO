from __future__ import annotations
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        return

def get_node(count) :
    print('讓我們將linked list資料列出來')
    node = node1
    for i in range (count):
        print (node.data,end=' ') 
        node = node.next

def remove_node() :
    print('讓我們移除第3個資料')
    node4.next = node3

def insert_node() :
    print('讓我們在node1和node2之間插入一個數字')
    print ('node4:',node4.data)
    node1.next = node4
    node4.next= node2

def append():
    print('讓我們放一些資料進linked list')
    
    cursor = node1
    while cursor.next:
        cursor = cursor.next

    cursor.next = node2

    cursor = node2
    while cursor.next:
        cursor = cursor.next

    cursor.next = node3
    print ('node1:',node1.data)
    print ('node2:',node2.data)
    print ('node3:',node3.data)
    
if __name__ == "__main__": 
    print()
    node1 = ListNode(12) 
    node2 = ListNode(99) 
    node3 = ListNode(37)
    append()
    print()
    get_node(3)
    print()
    print()
    node4 = ListNode(1)
    insert_node()
    print()
    get_node(4)
    print()
    print()
    remove_node()
    print()
    get_node(3)
