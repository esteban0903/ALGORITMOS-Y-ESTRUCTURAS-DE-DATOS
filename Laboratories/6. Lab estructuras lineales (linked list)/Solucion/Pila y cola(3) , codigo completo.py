class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def getValue(self):
        return self.value

    def setValue(self, new_value):
        self.value = new_value

    def getNext(self):
        return self.next

    def setNext(self, new_next):
        if isinstance(new_next, Node) or new_next is None:
            self.next = new_next
        else:
            raise Exception("New Next must be Node")

    def getPrev(self):
        return self.prev

    def setPrev(self, new_prev):
        if isinstance(new_prev, Node) or new_prev is None:
            self.prev = new_prev
        else:
            raise Exception("New Next must be Node")

    def clear(self):
        self.value = None
        self.next = None
        self.prev = None

    def __str__(self):
        next = self.next
        return "Node(" + str(self.value) + ") -->" + ("x" if next is None else str(next))


class LinkedList:
    def __init__(self, data=[]):
        self.head, self.tail, self.prev, self.len = None, None, None, 0
        for e in data:
            self.append(e)

    def __len__(self):
        return self.len

    def append(self, value):
        new_node = Node(value)
        if len(self) == 0:
            self.head = new_node
            self.setTail(new_node)
        else:
            current_tail = self.tail
            current_tail.setNext(new_node)
            new_node.setPrev(current_tail)  # Establecer la referencia al nodo anterior
            self.setTail(new_node)
        self.len = self.len + 1

    def append_stack(self, value):
        new_node = Node(value)
        if len(self) == 0:
            self.head = new_node
            self.setTail(new_node)
        else:
            new_node.setNext(self.head)
            self.head = new_node
        self.len = self.len + 1
    def search(self, value):
        current = self.head
        while current is not None and current.getValue() != value:
            current = current.getNext()
        return current

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def setTail(self, new_tail):
        if new_tail is not None:
            new_tail.setNext(None)
            self.tail = new_tail
        else:
            self.tail = None

    def getPrev(self):
        return self.prev

    def setPrev(self, new_prev):
        if isinstance(new_prev, Node) or new_prev is None:
            self.prev = new_prev
        else:
            raise Exception("New Next must be Node")

    def update(self, old_value, new_value):
        node_origin = self.search(old_value)
        node_origin.setValue(new_value)

    def slice(self, value, n=1):
        ld = LinkedList()
        node_origin = self.search(value)
        if node_origin is not None:
            current, index = node_origin, 0
            while current is not None and index < n:
                ld.append(current.getValue())
                current = current.getNext()
                index += 1
        return ld

    def isEmpty(self):
        return len(self) == 0

    def merge(self, list_b):
        if self.isEmpty():
            return list_b
        if list_b.isEmpty():
            return self
        self.tail.setNext(list_b.getHead())
        self.setTail(list_b.getTail())

    def delete(self, value):
        if self.isEmpty():
            return None
        current_node = self.head.getNext()
        prev = self.head
        # CABEZA
        if prev.getValue() == value:
            self.head = self.head.getNext()
            if self.isEmpty():
                self.tail = None
            self.len += -1

        while current_node is not None and (current_node.getValue() != value):
            prev = current_node
            current_node = current_node.getNext()
        # ELEMENTO
        if current_node is not None:
            if current_node.getNext() is None:
                self.tail = prev
            prev.setNext(current_node.getNext())
            self.len += -1
        else:
            raise Exception("Element not found.")
    def __str__(self):
        rep_str = ""
        return str(self.getHead())


class Queue:
    def __init__(self, lista=None):
        if lista is None:
            lista = []
        self.data = LinkedList(lista)

    def enqueue(self, e):
        self.data.append(e)

    def dequeue(self):
        if self.data.isEmpty():
            return None
        else:
            self.data.head = self.data.head.getNext()
            self.data.len -= 1
            if self.data.isEmpty():
                self.data.tail=None

    def __str__(self):
        return "Queue(" + str(self.data) + ")"

    def __len__(self):
        return len(self.data)

class Stack:
    def __init__(self, lista=[]):
        self.data = LinkedList(lista)

    def push(self, e):
        self.data.append(e)

    def pop(self):
        if self.data.isEmpty():
            return None
        else:
            self.data.setTail(self.data.getTail().getPrev())
            self.data.len -= 1

    def __str__(self):
        return "Stack(" + str(self.data) + ")"

    def __len__(self):
        return len(self.data)


def main():
    """list = LinkedList([i for i in range(1000)])
    print(len(list))
    current = list.getHead()
    # print(current)
    for e in range(len(list)):
        # print(current.getValue())
        current = current.getNext()
    search_result = list.search(900)
    # print("Buscando un valor", search_result.getValue() if search_result is not None else "Not found")
    slc = list.slice(900, 5)
    # print(slc.getHead())
    list_a = LinkedList([i for i in range(10000)])
    list_b = LinkedList([i for i in range(10000, 100000)])
    list_a.merge(list_b)
    print(list_a.getTail())"""
    lista = [1, 2, 3]
    lista1 = Stack(lista)
    lista2 = Queue(lista)
    print(lista1)
    print(lista2)



main()