# -*- coding:utf-8 -*-
class chainList():
    def __init__(self, value=None, next=None):  # 空表表头
        self.value = value
        self.next = next

    @property
    def Value(self):  # 给链表单元赋值
        return self.value

    @Value.setter
    def Value(self, v):
        self.value = v

    @property
    def Next(self):  # 链接下一个元素
        return self.next

    @Next.setter
    def Next(self, n):
        self.next = n


def FindKth(k, chain_list):
    index = 0  # 起始序列号为0
    element = chain_list.Next  # 将指针指向第一个链表单元
    while index != k and element is not None:  # 若找到k，或者到表尾，循环退出
        index += 1
        element = element.Next
    if index == k:  # 找到返回元素的值
        return element
    else:  # 没有返回 None
        return None


def Find(x, chain_list):
    index = 0  # 起始序列号为0
    element = chain_list.Next  # 将指针指向第一个链表单元
    while element.Value != x and element is not None:  # 若找到x，或者到表尾，循环退出
        index += 1
        element = element.Next
    if element.Value == x:  # 找到返回元素的值
        return index
    else:  # 没有返回 None
        return None


def Insert(x, index, chain_list):
    element = chain_list(x)  # 生成新节点
    if index == 0 :  # 遇到头节点的话则直接插入到头节点前
        element.Next = chain_list
        return element
    elementBefore = FindKth(index - 1, L)  # 查找序列前一个节点
    if elementBefore is not None:
        temp = elementBefore.Next
        elementBefore.Next = element  # 将新节点插在index－1
        节点后
        element.Next = temp  # 将原来的index节点插在新节点后
        del temp  # 释放内存
        return chain_list #返回头指针
    else:
        return '参数错误'


def Delete(index, chain_list):
    if index == 0:  # 遇到头节点的话则直接删除头节点
        p = chain_list.Next
        del chain_list
        return p
    elementBefore = FindKth(Index - 1, chain_list)  # 查找序列前一个节点
    if elementBefore is not None:
        temp = elementBefore.Next  # 将指针指向要删除的节点
        elementBefore.Next = temp.Next  # 将index－1节点指向index＋1节点
        del temp  # 释放内存
        return chain_list # 返回头指针
    else:
        return '参数错误'


def Length(chain_list):
    p = chain_list  # p指向第一个节点
    count = 0
    while p.Next is not None:  # p不断指向下一个节点
        count += 1
        p = p.Next

    return count

