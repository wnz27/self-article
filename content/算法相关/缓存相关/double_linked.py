'''
Date: 2020-09-10 16:36:07
LastEditTime: 2020-09-10 16:41:02
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


