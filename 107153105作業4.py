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

def is_empty() :
    if node1.data is 0:
        print("linked list has element? no")
    else:
        print("linked list has element? yes")

def remove_node() :
    print('讓我們移除node2')
    node1.next = node3 
    
if __name__ == "__main__":
    node1 = ListNode(0) 
    is_empty()
    print()
    print('讓我們放一些資料進linked list')
    node1 = ListNode(12) 
    node2 = ListNode(99) 
    node3 = ListNode(37)
    node1.next = node2 
    node2.next = node3
    print ('node1:',node1.data)
    print ('node2:',node2.data)
    print ('node3:',node3.data)
    print()
    is_empty()
    print()
    get_node(3)
    print()
    print()
    remove_node()
    print()
    get_node(2)
