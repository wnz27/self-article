'''
Date: 2020-09-10 16:36:07
LastEditTime: 2020-09-11 13:00:14
'''
# -*- coding:utf-8 -*-

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        val = "\{{}:{}\}".format(self.key, self.value)
        return val
    
    def __repr__(self):
        val = "\{{}:{}\}".format(self.key, self.value)
        return val
    
class DoubleLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0

if __name__ == '__main__':
    import json
    a = {1: "123", 2: "34343"}
    b = json.dumps(a)
    print(b, type(b))
    c = json.loads(b)
    print(c)
