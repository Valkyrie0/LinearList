class stackChain():
    def __init__(self, value=None, next=None):  # 创建一个空链表
        self.value = value
        self.next = next


def isEmpty(stack_chain):  # 判断堆栈是否为空
    return stack_chain.next is None


def push(stack_chain, element):  # 向堆栈stack_chain中插入元素element,并返回头指针
    newChain = stackChain()  # 生成新的链表元素
    newChain.next = stack_chain.next  # 将原表头下一个元素的地址赋值给新的链表元素
    newChain.value = stack_chain.value  # 将原表头的值复制给新的元素
    print('push  %d in stack' % element)
    stack_chain.next = newChain  # 对头元素进行更新
    stack_chain.value = element
    return stack_chain


def pop(stack_chain):  # 堆栈stack_chain的头元素,并返回头指针
    if isEmpty(stack_chain):
        print('it is an empty stack')
    else:
        print('pop %d out from stack' % stack_chain.value)
        temp = stack_chain.next
        stack_chain.next = temp.next
        stack_chain.value = temp.value
        del temp
    return stack_chain

test = stackChain()
isEmpty(test)
push(test,1)
push(test,2)
push(test,3)
pop(test)
pop(test)