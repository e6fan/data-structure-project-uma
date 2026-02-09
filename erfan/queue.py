class QueueCircular:
      def  __init__(self,num):
        self.num=num
        self.data=[None]*num
        self.front=-1
        self.rear=-1
      def is_Full(self):
          if (((self.rear+1)%self.num==self.front) or (self.rear==-1 and self.front==0)):
            return True
          else:
              return False
      def is_Empty(self):
          if self.front==-1:
              return True
          else :
              return False
      def Enqueue(self,p):
          if self.is_Full():
              print ("the queue is full")
              return
          if self.is_Empty():
             self.front=0
          self.rear=(self.rear+1)%self.num
          self.data[self.rear]=p

      def  Dequeue(self): 
          if self.is_Empty():
              print("the queue is empty")
              return
          else:
            v=self.data[self.front]
            self.front=(self.front +1)%self.num
            return v 
      def Peek(self):
           x=self.data[self.front]
           return x     
      def ReverseQueue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = [None] * self.num
        i = self.front
        k = 0
        while True:
            temp[k] = self.data[i]
            k += 1
            if i == self.rear:
                break
            i = (i + 1) % self.num
        self.front = 0
        self.rear = -1
        reversed = [None] * k
        for j in range(k - 1, -1, -1):
              self.Enqueue(temp[j])
              reversed[k-j-1]=temp[j]
        return temp[j]     