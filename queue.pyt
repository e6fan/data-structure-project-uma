class Queue:
    def __init__(self,size):
        self.queue=[None]*size
        self.end=-1
        self.size=size
    def enqueue(self,value):
        if (self.end==self.size):
            self.is_full()
        else:
            self.end+=1
            self.queue[self.end]=value
    def dequeue(self):
        if self.end==-1:
            self.is_empty()
        else:
            for i in range(self.size-1):
                m=self.queue[i+1]
                self.queue[i]=m
    def peek(self):
        return self.queue[0]
    def revers(self):
        first=0
        last=self.size-1
        while first<last:
            self.queue[first],self.queue[last]=self.queue[last],self.queue[first]
            first+=1
            last-=1
    def is_empty(self):
        print("queue is empty")
    def is_full(self):
        print("queue is full")
s=Queue(4)
s.enqueue(1)
s.enqueue(2)
s.enqueue(7)
print(s.queue)
s.dequeue()
print(s.queue)
print(s.peek())
s.revers()
print(s.queue)