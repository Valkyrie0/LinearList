# -*- coding: utf-8 -*-

class polyNode():
    def __init__(self, coef, expon, next=None):  # 构建链表单元结构
        self.coef = coef
        self.expon = expon
        self.next = next


# ---------------队列定义--------------------------------
class queueChain:
    def __init__(self, front=None, rear=None):
        self.front = front  # fron指向表头的指针
        self.rear = rear  # rear指向表尾的指针


def inQue(queue, newNote):  # 入队操作
    if queue.front is None:  # 链表为空,将front 赋值给表头
        queue.front = queue.rear = newNote
    else:
        queue.rear.next = newNote
        queue.rear = newNote


def outQue(queue):  # 出队操作
    if queue.front is None:  # 如果front指向为空,则链表为空
        print('it is an empty queue!')
    else:
        p = queue.front
        if queue.front == queue.rear:  # 如果前后指针指向一个元素,则全部重置为None
            queue.front = queue.rear = None
        else:
            queue.front = p.next
        return p


# -------------------------加法定义-------------------

def polyAdd(ps1, ps2):
    storePoly = queueChain()  # 构建存放结果的队列
    p1 = ps1.front  # 构建 p1,p2分别指向存放元素的表头
    p2 = ps2.front
    while p1 is not None and p2 is not None:
        compare = p1.expon - p2.expon  # 对比两者指数的大小
        if compare > 0:  # 如果n1的指数大
            inQue(storePoly, p1)
            p1 = p1.next  # 将指针指向p1下一个元素
        elif compare < 0:  # 如果n2的指数大
            inQue(storePoly, p2)
            p2 = p2.next  # 将指针指向p2下一个元素
        else:
            if p1.coef + p2.coef or not(p1.expon):  # 未抵消则入队
                newNote = polyNode(p1.coef + p2.coef, p1.expon)  # 入队
                inQue(storePoly, newNote)
            p1 = p1.next
            p2 = p2.next
    while p1 is not None:
        inQue(storePoly, p1)
        p1 = p1.next
    while p2 is not None:
        inQue(storePoly, p2)
        p2 = p2.next
    return storePoly


# -------------------------乘法法定义-------------------
def polyMultiple(ps1, ps2):
    storePoly = queueChain()
    p1 = ps1.front  # 构建 p1,p2分别指向存放元素的表头
    p2 = ps2.front
    while p1 is not None:  # 将p1中的元素逐个弹出
        tag = p2  # tag 指向p2的头指针,用于循环相乘
        newP2 = queueChain()  # 存放一次相乘结果的队列
        while tag is not None:  # 将爬p1弹出的元素逐个与p2中的元素相乘
            inQue(newP2, polyNode(coef=p1.coef * tag.coef, expon=p1.expon + tag.expon))
            tag = tag.next
        p1 = p1.next
        storePoly = polyAdd(newP2, storePoly)
    return storePoly


# --------------------输入输出定义----------------------

def inputPoly(li):  # 将输入的字符串转化为链表
    poly = queueChain()
    del li[0]
    while len(li) != 0:
        inQue(poly, polyNode(li[0], li[1]))
        del li[0:2]
    return poly


def outputPoly(queue_chain):
    fr = queue_chain.front
    while fr.next is not None:
        print(str(fr.coef)+' '+str(fr.expon),end=' ')
        fr = fr.next
    print(str(fr.coef)+' '+str(fr.expon))

#multinomial1 = list(map(int, input().split()))
#multinomial2 = list(map(int, input().split()))
multinomial1 =[1,2,0,]
multinomial2 =[1,2,0,0,0]

pr1 = inputPoly(multinomial1)
pr2 = inputPoly(multinomial2)

result = polyMultiple(pr1, pr2)
outputPoly(result)
result = polyAdd(pr1, pr2)
outputPoly(result)

