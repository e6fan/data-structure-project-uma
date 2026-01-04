class Node:
    def __init__(self,data):
        self.data=data
        self.next=Node
class circularlinklist:
    def __init__(self):
        self.head=None
    def insertatindex(self,data,index):
        if index<0:
            print("indext cant be negetive")
        if index==0:
            n_node=Node(data)
            if self.head==None:
                self.head=n_node
                n_node.next=self.head
            else:
                cur=self.head
                while cur.next!=self.head:
                    cur=cur.next
                n_node=self.head
                cur.next=n_node
                self.head=n_node
        else:
            n_node=Node(data)
            x=0
            cur=self.head
            while(x<index-1):
                cur=cur.next
                x+=1
            n_node.next=cur.next
            cur.next=n_node
    def Addtobegin(self,data):
        n_node=Node(data)
        if self.head==None:
            self.head=n_node
            n_node.next=self.head
        else:
            cur=self.head
            while cur.next!=self.head:
                cur=cur.next
            n_node.next=self.head
            cur.next=n_node
            self.head=n_node
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
    def deletatbegin(self):
        if self.head==None:
            print("list is empyu")
        cur=self.head.data
        if self.head.next==self.head:
            self.head=None
        else:
            last=self.head
            while last.next!=self.head:
                last=last.next
            self.head=self.head.next
            last.next=self.head
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
        
    def deleteatindex(self,index):
        if self.head==None:
            print(";ist is empty")
        if index<0:
            print("index cant be negetive")
        if index==0:
            if self.head.next==self.head:
                self.head=None
            else:
                last=self.head
                while last.next!=self.head:
                    last=last.next
                self.head=self.head.next
                last.next=self.head
        cur=self.head
        x=0
        while x<index-1:
            cur=cur.next
            x+=1
        cur.next=cur.next
    def updatenode(self,n_data,index):
        if self.head==None:
            print("list is empty")
        if index<0:
            print("index cant be negetive")
        cur=self.head
        x=0
        while True:
            if x==index:
                cur.data=n_data
            cur=cur.next
            x+=1
            if x==self.head:
                break
    def sizeoflist(self):
        if self.head==None:
            return 0
        x=1
        cur=self.head
        while cur.next!=self.head:
            cur=cur.next
            x+=1
        return x
    def invert(self):
        if self.head==None:
            print("this list dont have a invert")
        prev=None
        cur=self.head
        n_node=None
        first_node=self.head
        while True:
            n_node=cur.next
            cur.next=prev
            prev=cur
            cur=n_node
            if cur==first_node:
                break
        self.head=prev
        first_node.next=self.head
    def concotenate(self,n_list):
        if n_list==None:
            print("your new list is empty")
        cur=self.head
        while cur.next!=self.head:
            cur=cur.next
        n_last=n_list.head
        while n_last.next!=n_list.head:
            n_last=n_last.next
        cur.next=n_list.head
        n_last.next=self.head
        n_list.head=None
    def display(self):
        cur=self.head
        while(cur):
            print(cur.data)
            cur=cur.next
            if cur==self.head:
                break
s=circularlinklist()
s.insertatindex(0,0)
s.insertatindex(1,1)
s.insertatindex(2,2)
s.Addtobegin(4)
s.Addtoend(6)
s.updatenode(9,1)
s.deleteatindex(0)
s.deletatbegin()
s.deletatend()
print(s.sizeoflist())
s.invert()
s.display()