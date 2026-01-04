class Node:
    def __init__(self,data):
        self.data=data
        self.next=Node
class circularlinklist:
    def __init__(self):
        self.head=None
    def Addtoend(self,data):
        n_node=Node(data)
        if self.head==None:
            self.head=n_node
            n_node.next=self.head
        else:
            cur=self.head
            while cur.next!=self.head:
                cur=cur.next
            cur.next=n_node
            n_node.next=self.head
    def deletatend(self):
        if self.head==None:
            print("list is empty")
        if self.head.next==self.head:
            remove=self.head.data
            self.head=None
            return remove
        prev=None
        cur=self.head
        while cur.next!=self.head:
            prev=cur
            cur=cur.next
        remove=cur.data
        prev.next=self.head
    def display(self):
        cur=self.head
        while(cur):
            print(cur.data)
            cur=cur.next
            if cur==self.head:
                break
class stack:
    stack=circularlinklist()
    def push(self,value):
        self.stack.Addtoend(value)
    def pop(self):
        self.stack.deletatend()
    def displaystack(self):
        self.stack.display()
s=stack()
s.push(1)
s.push(2)
s.pop()
print(s.displaystack())