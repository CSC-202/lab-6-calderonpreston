

class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
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


def initialize() -> Stack:
    #raise NotImplementedError("Stack.initialize() not defined")
    return Stack

def isEmpty(data: Stack) -> bool:
    #raise NotImplementedError("Stack.isEmpty() not defined")
    if data.first == None:
        return True
    else:
        return False

def push(data: Stack, value: int) -> Stack:
    #raise NotImplementedError("Stack.push() not defined")
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
# data = Stack()
# data.first = Node(1,Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
# print(data.toPythonList())
# print(push(data, 500).toPythonList())

def pop(data: Stack) -> tuple[Node, Stack]:
    #raise NotImplementedError("Stack.pop() not defined")
    length: int = len(data) - 1
    if length == 0:
        data.first = data.first.next
        return data
    def helper(v: Node, index: int, i:int):
        if i == index - 1:
            v.next = v.next.next
            return data
        elif i > index:
            raise IndexError('no bueno')
        else:
            return helper(v.next, index, i+1)
    if isEmpty(data) == True:
        return None
    elif length < 0 or length >= len(data):
        raise IndexError('no tengo')
    else:
        return helper(data.first, length,  i = 0)


#GOOD
# data = Stack()
# data.first = None
# print(data.toPythonList())
# print(pop(data).toPythonList())


def peek(data: Stack) -> Node:
    #raise NotImplementedError("Stack.peek() not defined")
    length: int = len(data) - 1
    def helper(v: Node, index: int, i:int):
        if i == index:
            return v
        elif i > index:
            raise IndexError('no bueno')
        else:
            return helper(v.next, index, i+1)
    if isEmpty(data) == True:
        return None
    elif length < 0 or length >= len(data):
        raise IndexError('no tengo')
    else:
        return helper(data.first, length, i = 0)

# Good
# data = Stack()
# data.first = Node(1,Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
# print(data.toPythonList())
# print(peek(data).value)

def clear(data: Stack) -> Stack:
    #raise NotImplementedError("Stack.clear() not defined")
    data.first = None
    return data
#Good