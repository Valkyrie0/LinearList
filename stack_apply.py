# -*- coding: utf-8 -*-

class newStack():
    def __init__(self, maxSize):
        self._maxSize = maxSize
        self._p1 = -1  # 堆栈1 的指针
        self._p2 = maxSize  # 堆栈2 的指针
        self._stack = [None] * maxSize  # 储存元素的数组

    def push(self, value, tag):  # 插入数据, tag表示插入哪一个堆栈堆栈
        if self._p2 - self._p1 == 1:  # 通过判断两个指针位置是否相邻,确定堆栈是否满了
            print('all stack are full')
        else:
            if tag == 1:
                self._p1 += 1  # 指针向中间移动
                self._stack[self._p1] = value
                print('push %d in stack1 ' % value)
            elif tag == 2:
                self._p2 -= 1  # 指针向中间移动
                self._stack[self._p2] = value
                print('push %d in stack2 ' % value)
            else:
                print("stack %d doesn't exist" % tag)

    def pop(self, tag):  # 删除数据
        if tag == 1:
            if self._p1 == -1:  # 通过判断指针位置来确定堆栈是否为空
                print("it's an empty stack1")
            else:
                iterm1 = self._stack[self._p1]  # 将最后一位元素的值取出
                self._stack[self._p1] = None  # 删除元素
                self._p1 -= 1  # 指针指向栈顶
                print('pop %d out from stack 1' % iterm1)
                return iterm1  # 返回最后一位元素的值
        elif tag == 2:
            if self._p2 == self._maxSize:  # 通过判断指针位置来确定堆栈是否为空
                print("it's an empty stack2")
            else:
                iterm2 = self._stack[self._p2]  # 将最后一位元素的值取出
                self._stack[self._p2] = None  # 删除元素
                self._p2 += 1  # 指针指向栈顶
                print('pop %d out from stack 2' % iterm2)
                return iterm2  # 返回最后一位元素的值
        else:
            print("stack %d doesn't exist" % tag)

test = newStack(4)
test.push(1,1)
test.push(2,1)
test.push(3,2)
test.push(4,2)
test.push(3,3)
test.push(4,2)
test.pop(1)
test.pop(2)