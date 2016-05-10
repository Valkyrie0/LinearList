# -*- coding:utf-8 -*-
class chainList():
    def __init__(self, value=None, next=None):  # 空表表头
        self.value = value
        self.next = next

def setup_chain(lists):  # 初始化列表
    list_chain = list(map(lambda x: chainList(x), lists))
    for i in range(0, len(list_chain)-1):
        list_chain[i].next = list_chain[i + 1]
    return list_chain[0]


def FindKth(k, chain_list):
    index = 0  # 起始序列号为0
    element = chain_list  # 将指针指向第一个链表单元
    while index != k and element.next is not None:  # 若找到k，或者到表尾，循环退出
        index += 1
        element = element.next
    if index == k:  # 找到返回元素的值
        return element
    else:  # 没有返回 None
        return None


def Find(x, chain_list):
    index = 0  # 起始序列号为0
    element = chain_list  # 将指针指向第一个链表单元
    while element.value != x and element.next is not None:  # 若找到x，或者到表尾，循环退出
        index += 1
        element = element.next
    if element.value == x:  # 找到返回元素的值
        return index
    else:  # 没有返回 None
        return None


def Insert(x, index, chain_list):
    element = chainList(x)  # 生成新节点
    if index == 0:  # 遇到头节点的话则直接插入到头节点前
        element.next = chain_list
        return element
    elementBefore = FindKth(index - 1, chain_list)  # 查找序列前一个节点
    if elementBefore is not None:
        temp = elementBefore.next
        elementBefore.next = element  # 将新节点插在index－1节点后
        element.next = temp  # 将原来的index节点插在新节点后
        del temp  # 释放内存
        return chain_list  # 返回头指针
    else:
        return '参数错误'


def Delete(index, chain_list):
    if index == 0:  # 遇到头节点的话则直接删除头节点
        p = chain_list.next
        del chain_list
        return p
    elementBefore = FindKth(index - 1, chain_list)  # 查找序列前一个节点
    if elementBefore is not None:
        temp = elementBefore.next  # 将指针指向要删除的节点
        elementBefore.next = temp.next  # 将index－1节点指向index＋1节点
        del temp  # 释放内存
        return chain_list  # 返回头指针
    else:
        return '参数错误'


def Length(chain_list):
    p = chain_list  # p指向第一个节点
    count = 0
    while p.next is not None:  # p不断指向下一个节点
        count += 1
        p = p.next

    return count

# 测试
'''initialChain = setup_chain([1,2,3,4])

print(FindKth(1,initialChain).value)
print(Find(2,initialChain))
afterInsert = Insert(0,2,initialChain)
print(FindKth(2,afterInsert).value)
afterDelete = Delete(2,afterInsert)
print(FindKth(2,afterInsert).value)
print(Length(afterDelete))
'''
