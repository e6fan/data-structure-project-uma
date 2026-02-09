class Stack:
    def __init__(self):
        self.items = []

    def Push(self, item):
        self.items.append(item)

    def Pop(self):
        if self.IsEmpty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def Peek(self):
        if self.IsEmpty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def IsEmpty(self):
        return len(self.items) == 0
