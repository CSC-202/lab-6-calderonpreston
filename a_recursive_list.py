class Node:
    value: any
    next: any

    def __init__(self, value, next):
        self.value = value
        self.next = next


class List:
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


def initialize() -> List:
    #raise NotImplementedError("List.initialize() not defined")
    return List

def isEmpty(data: List) -> bool:
    #raise NotImplementedError("List.isEmpty() not defined")
    return data.first == None and data.last == None

# GOOD
# data = List()
# data.first = None
# print(isEmpty(data))



def addAtIndex(data: List, index: int, value: int) -> List:
    if index == 0:
        if isEmpty(data):
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
    elif index < 0 or index >= len(data) + 1:
        raise IndexError('no tengo')
    else:
        return helper(data.first, index, i = 0)
# GOOD!
# data = List()
# data.first = Node(1,Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
# print(data.toPythonList())
# print(addAtIndex(data, 0, 500).toPythonList())


def removeAtIndex(data: List, index: int) -> tuple[Node, List]:
    #raise NotImplementedError("List.removeAtIndex() not defined")
    if index == 0:
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
    if isEmpty(data):
        return None
    elif index < 0 or index >= len(data):
        raise IndexError('no tengo')
    else:
        return helper(data.first, index, i = 0)
#GOOD
# data = List()
# data.first = Node(1,Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
# print(data.toPythonList())
# print(removeAtIndex(data, 0).toPythonList())


def addToFront(data: List, value: int) -> List:
    #raise NotImplementedError("List.addToFront() not defined")
    if isEmpty(data):
        data.first = Node(value, None)
        return data
    else:
        new_node = Node(value, data.first)
        data.first = new_node
        return data

# GOOD
# data = List()
# data.first = Node(1,Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
# print(data.toPythonList())
# print(addToFront(data, 1000).toPythonList())



def addToBack(data: List, value: int) -> List:
    #raise NotImplementedError("List.addToBack() not defined")
    if isEmpty(data):
        addToFront(data, value)
        return data
    else:
        addAtIndex(data, len(data), value)
        return data
# GOOD
# data = List()
# data.first = None
# print(data.toPythonList())
# print(addToBack(data, 1000).toPythonList())

def getElementAtIndex(data: List, index: int, counter = 0) -> Node:
    #raise NotImplementedError("List.getElementAtIndex() not defined")
    def helper(v: Node, index: int, i:int):
        if i == index:
            return v
        elif i > index:
            raise IndexError('no bueno')
        else:
            return helper(v.next, index, i+1)
    if isEmpty(data):
        return None
    elif index < 0 or index >= len(data):
        raise IndexError('no tengo')
    else:
        return helper(data.first, index, i = 0)

# Good
# data = List()
# data.first = Node(1,Node(2, Node(3, Node(4, Node(5, Node(6, None))))))
# print(data.toPythonList())
# print(getElementAtIndex(data, 1).value)

def clear(data: List) -> List:
    #raise NotImplementedError("List.clear() not defined")
    data.first = None
    return data

