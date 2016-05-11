# -*- coding: utf-8 -*-

class Stack():
    def __init__(self, maxSize):  # 初始化堆栈,设定最大值
        self._stack = []
        self._maxSize = maxSize
        self._p = -1  # 指针指向栈顶

    def push(self, value):  # 插入数据
        if self._p >= self._maxSize-1:  # 通过判断指针位置是否超过初始容量,确定堆栈是否满了
            print('stack is full')
        else:
            self._stack.append(value)
            self._p += 1  # 指针向栈顶移动
            print('push %d in stack ' % value)

    def pop(self): # 删除数据
        if self._p == -1:  # 通过判断指针位置来确定堆栈是否为空
            print("it's an empty stack")
        else:
            iterms = self._stack[-1]  # 将最后一位元素的值取出
            del self._stack[self._p]  # s删除元素
            self._p -= 1  # 指针指向栈顶
            print('pop %d out' % iterms)
            return iterms  # 返回最后一位元素的值


test = Stack(4)
test.push(1)
test.push(2)
test.push(3)
test.push(4)
test.push(5)
test.pop()
test.pop()
test.pop()
test.pop()
test.pop()
test.pop()
