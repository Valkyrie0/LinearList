class stackChain():
    def __init__(self, value=None, next=None):  # 创建一个空链表
        self.value = value
        self.next = next


def isEmpty(stack_chain):  # 判断堆栈是否为空
    return stack_chain.next is None


def push(stack_chain, element):  # 向堆栈stack_chain中插入元素element,并返回头指针
    newChain = stackChain(element) # 生成新的链表元素
    newChain.next = stack_chain.next  # 将原表头栈顶元素接到新元素的下面
    stack_chain.next = newChain  # 将头指针指向新元素
    print('push '+str(element)+' in stack')
    return stack_chain


def pop(stack_chain):  # 堆栈stack_chain的头元素,并返回弹出的元素
    if isEmpty(stack_chain):
        print('it is an empty stack')
    else:
        p = stack_chain.next  # 指针指向头一个元素
        print('pop '+str(p.value)+' out from stack')
        stack_chain.next = p.next  # 将指针指向栈顶元素
        element = p.value
        del p  # 释放空间
    return element
'''
test = stackChain()
isEmpty(test)
push(test,1)
push(test,2)
push(test,3)
pop(test)
pop(test)
'''