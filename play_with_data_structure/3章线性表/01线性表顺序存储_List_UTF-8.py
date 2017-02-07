#!/usr/bin/env python
# -*- coding:utf-8 -*-

ERROR = 0
OK = 1

class SequenceList(object):
    """线性表顺序储存
    >>> s = SequenceList()
    >>> s.list_empty()
    True
    >>> s.list_insert(0, 0)
    1
    >>> s.list_insert(1, 1)
    1
    >>> s.list_insert(2, 2)
    1
    >>> s.list_insert(3, 3)
    1
    >>> s.list_insert(4, 99)
    1
    >>> s.list_length()
    5
    >>> s.get_elem(4)
    99
    >>> s.locate_elem(2)
    2
    >>> s.list_delete(2)
    1
    >>> s.list_length()
    4
    >>> s.list_traverse()
    0
    1
    3
    99
    >>> s.clear_list()
    1
    >>> s.list_length()
    0
    """

    MAX_SIZE = 50

    def __init__(self):
        self.data = []
        self.length = 0

    def list_empty(self):
        return self.length == 0

    def clear_list(self):
        self.data = []
        self.length = 0
        return OK

    def list_length(self):
        return self.length

    def get_elem(self, index):
        if 0 < index < self.length:
            return self.data[index]
        return ERROR

    def locate_elem(self, elem):
        try:
            return self.data.index(elem)
        except ValueError:
            return -1

    def list_insert(self, index, elem):
        if self.length == self.MAX_SIZE:
            return ERROR
        self.data.insert(index, elem)
        self.length += 1
        return OK

    def list_delete(self, index):
        if index < 0 or index > self.length - 1:
            return ERROR
        del self.data[index]
        self.length -= 1
        return OK

    def list_traverse(self):
        for i in self.data:
            print i


if __name__ == '__main__':
    import doctest
    doctest.testmod()
