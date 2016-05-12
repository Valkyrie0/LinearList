# -*- coding: utf-8 -*-
''''
class Queue():  # 基础实现
    def __init__(self, maxSize):  # 初始化队列,头和尾都指向-1
        self._front = -1
        self._rear = -1
        self._q = [None] * maxSize

    def addElem(self, element):
        if self._rear == len(self._q) - 1:  # 如果rear指向了队列的最后一个元素,则队列满了
            print('it is a full queue!')
        else:
            self._rear += 1
            self._q[self._rear] = element
            print('add ' + str(element) + ' in Queue')

    def deleteElem(self):  # 删除front指向的元素,并放回被删除的元素
        if self._front == self._rear:  # 如果front 和 rear指向同一个元素,则队列为空
            print('it is an empty queue!')
        else:
            self._front += 1
            value = self._q[self._front]
            print('delete ' + str(value) + ' out of Queue')
            self._q[self._front] = None  # 删除元素
            return value
'''

class Queue():  # 顺环实现
    def __init__(self, maxSize):  # 初始化队列,头和尾都指向-1
        self._front = 0
        self._rear = 0
        self._q = [None] * maxSize

    def addElem(self, element):
        if (self._rear + 1) % len(self._q) == self._front:  # 对rear进行加一取余数(实现循环利用),但到达最大数时归到起始位置即0,1,2,3,4,0,1,2,3,4依次循环
            print('it is a full queue!')
        else:
            self._q[self._rear] = element
            self._rear = (self._rear + 1) % len(self._q)
            #print(str(self._rear)+'----'+str(self._front))
            print('add ' + str(element) + ' in Queue')

    def deleteElem(self):  # 删除front指向的元素,并放回被删除的元素
        if self._front == self._rear:  # 如果front 和 rear指向同一个元素,则队列为空
            print('it is an empty queue!')
        else:
            value = self._q[self._front]
            self._q[self._front] = None  # 删除元素
            self._front = (self._front + 1) % len(self._q)  # 对rear进行加一取余数(实现循环利用),但到达最大数时归到起始位置
            print('delete ' + str(value) + ' out of Queue')
            return value


test = Queue(4)

test.addElem(1)
test.addElem(2)
test.addElem(3)
test.addElem(4)
test.addElem(5)
test.deleteElem()
test.deleteElem()
test.deleteElem()
test.addElem(2)
test.addElem(3)
test.deleteElem()
test.deleteElem()
test.deleteElem()
