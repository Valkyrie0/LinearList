class Note():
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class queueChain:
    def __init__(self,front=None,rear=None):
        self.front = front # fron指向表头的指针
        self.rear = rear # rear指向表尾的指针

def inQue(queue, value):  # 入队操作
    newNote = Note(value)
    if queue.front is None:  # 链表为空,将front 赋值给表头
        queue.front = queue.rear =  newNote
    else:
        queue.rear.next = newNote
        queue.rear = newNote
    print('add  '+str(value)+' in the queue' )

def outQue(queue): # 出队操作
    if queue.front is None :  # 如果front指向为空,则链表为空
        print('it is an empty queue!')
    else:
        p = queue.front
        element = p.value
        if queue.front == queue.rear:  # 如果前后指针指向一个元素,则全部重置为None
            queue.front = queue.rear = None
        else:
            queue.front = p.next
            del p  # 释放空间
        print('delete  ' + str(element) +'  out of Queue')
        return element


test = queueChain()
inQue(test,1)
inQue(test,2)
inQue(test,3)
inQue(test,4)
a = test.front
while a is not None:
    print(a.value)
    a = a.next
outQue(test)
outQue(test)
outQue(test)
outQue(test)
a = test.front
while a is not None:
    print(a.value)
    a = a.next