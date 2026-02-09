class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DualLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def InsertAtBegin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1
    def InsertAtEnd(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1
    def InsertAtIndex(self, data, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        if index == 0:
            self.InsertAtBegin(data)
            return
        if index == self.size:
            self.InsertAtEnd(data)
            return

        new_node = Node(data)
        current = self.head

        for _ in range(index):
            current = current.next

        prev_node = current.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = current
        current.prev = new_node

        self.size += 1
    def UpdateNode(self, data, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        current = self.head
        for _ in range(index):
            current = current.next

        current.data = data
    def RemoveNodeAtBegin(self):
        if self.head is None:
            raise IndexError("List is empty")

        removed_data = self.head.data

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
        return removed_data
    def RemoveNodeAtEnd(self):
        if self.tail is None:
            raise IndexError("List is empty")

        removed_data = self.tail.data

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        return removed_data
    def RemoveNodeAtIndex(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        if index == 0:
            return self.RemoveNodeAtBegin()
        if index == self.size - 1:
            return self.RemoveNodeAtEnd()

        current = self.head
        for _ in range(index):
            current = current.next

        removed_data = current.data
        current.prev.next = current.next
        current.next.prev = current.prev

        self.size -= 1
        return removed_data
    def SizeOfList(self):
        return self.size
    def Concatenate(self, other_list):
        if other_list.head is None:
            return

        if self.head is None:
            self.head = other_list.head
            self.tail = other_list.tail
        else:
            self.tail.next = other_list.head
            other_list.head.prev = self.tail
            self.tail = other_list.tail

        self.size += other_list.size


        