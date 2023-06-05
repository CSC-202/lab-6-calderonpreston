class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Queue:
    first: Node
    last: Node

    def __init__(self):
        self.first = None
        self.last = None

    def __len__(self):
        n: int = 0
        current = self.first
        while current != None:
            n += 1
            current = current.next
        return n

    def toPythonList(self):
        result: list = []
        current = self.first
        while current != None:
            result.append(current.value)
            current = current.next
        return result


def initialize() -> Queue:
    #raise NotImplementedError("Queue.initialize() not defined")
    return Queue

def isEmpty(data: Queue) -> bool:
    #raise NotImplementedError("Queue.isEmpty() not defined")
    if data.first == None:
        return True
    else:
        return False

def enqueue(data: Queue, value: int) -> Queue:
    #raise NotImplementedError("Queue.enqueue() not defined")
    length: int = len(data)
    if length == 0:
        if isEmpty(data) == True:
            data.first = Node(value, None)
            return data
        else:
            new_node = Node(value, data.first)
            data.first = new_node
            return data
    new_node = Node(value, next)
    def helper(v: Node, index: int, i:int):
        if i == index - 1:
            new_node.next = v.next
            v.next = new_node
            return data
        elif i > index:
            raise IndexError('no bueno')
        else:
            return helper(v.next, index, i+1)
    if isEmpty(data) == True:
        return None
    elif length < 0 or length >= length + 1:
        raise IndexError('no tengo')
    else:
        return helper(data.first, length, i = 0)
    
#GOOD
# data = Queue()
# data.first = Node(1,Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
# print(data.toPythonList())
# print(enqueue(data, 500).toPythonList())
# print(enqueue(data, 2500).toPythonList())


def dequeue(data: Queue) -> tuple[Node, Queue]:
    #raise NotImplementedError("Queue.dequeue() not defined")
    if isEmpty(data) == True:
            return None
    else:
        value = data.first.value
        next_node = data.first.next
        data.first.next = None
        data.first = next_node
        return [value, data.toPythonList()]


#GOOD
# data = Queue()
# data.first = Node(1,Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
# print(data.toPythonList())
# print(dequeue(data))

def peek(data: Queue) -> Node:
    #raise NotImplementedError("Queue.peek() not defined")
    return data.first.value

def clear(data: Queue) -> Queue:
    #raise NotImplementedError("Queue.clear() not defined")
    return Queue()