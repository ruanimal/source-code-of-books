#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Node(object):
    def __init__(self, data=None, next_=None):
        self.data = data
        if next_ is not None and not isinstance(next_, Node):
            raise ValueError('next must be a Node!')
        self.next = next_


class LinkList(object):
    """线性表链式存储
    >>> ll = LinkList()
    >>> for i in 'abcdef':
    ...     ll.list_insert(0, i)
    >>> ll.list_traverse()
    'f e d c b a'
    >>> ll.list_empty()
    False
    >>> ll.list_length()
    6
    >>> ll.get_elem(2)
    'd'
    >>> ll.locate_elem('a')
    5
    >>> ll.list_delete(3)
    >>> ll.list_traverse()
    'f e d b a'
    >>> ll.clear_list()
    >>> ll.list_empty()
    True
    """

    def __init__(self):
        self.head = Node()

    def list_empty(self):
        return self.head.next is None

    def clear_list(self):
        self.head = Node()

    def list_length(self):
        count = 0
        pointer = self.head.next
        while pointer:
            count += 1
            pointer = pointer.next
        return count

    def get_elem(self, index):
        i = 0
        pointer = self.head.next
        while pointer and index > i:
            pointer = pointer.next
            i += 1
        if pointer is None:
            raise IndexError
        return pointer.data

    def locate_elem(self, elem):
        i = 0
        pointer = self.head.next
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        return -1

    def list_insert(self, index, elem):
        i = 0
        pointer = self.head
        while pointer:
            if i == index:
                pointer.next = Node(elem, pointer.next)
                break
            pointer = pointer.next
            i += 1
        else:
            raise IndexError

    def list_delete(self, index):
        i = 0
        pointer = self.head.next
        while pointer:
            if i == index-1:
                if pointer.next is None:
                    raise IndexError
                pointer.next = pointer.next.next
                break
            pointer = pointer.next
            i += 1
        if pointer is None:
            raise IndexError

    def list_traverse(self):
        pointer = self.head.next
        tmp = []
        while pointer:
            tmp.append(str(pointer.data))
            pointer = pointer.next
        return ' '.join(tmp)

    def __str__(self):
        return '<LinkList>: [%s]' % self.list_traverse()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
