#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""原始代码的命名和继承关系很糟糕, DefaultFormatter继承Publisher真是不知所谓
1. 对象的状态变化能够通知所有相关者(观察者)
2. 观察者和观察者的数量是可以变化的
"""


class Publisher:

    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to add: {}'.format(observer))

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))

    def push(self, obj):
        # 不需要通知obj自身
        [o.notify(obj) for o in self.observers if o != obj]


class DefaultFormatter(object):

    def __init__(self, name, publisher):
        self.publisher = publisher
        self.name = name
        self._data = 0

    def __str__(self):
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name, self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.publisher.push(self)

    def notify(self, *args):
        print(self)

class HexFormatter(object):

    def notify(self, obj):
        print("{}: '{}' has now hex data = {}".format(type(self).__name__,
                                                      obj.name, hex(obj.data)))


class BinaryFormatter(object):

    def notify(self, obj):
        print("{}: '{}' has now bin data = {}".format(type(self).__name__,
                                                      obj.name, bin(obj.data)))


def main():
    p = Publisher()
    df = DefaultFormatter('test1', p)
    p.add(df)

    hf = HexFormatter()
    p.add(hf)
    df.data = 3

    bf = BinaryFormatter()
    p.add(bf)
    df.data = 21

    p.remove(hf)
    df.data = 40

    p.remove(hf)
    p.add(bf)
    df.data = 'hello'

    df.data = 15.8

if __name__ == '__main__':
    main()
