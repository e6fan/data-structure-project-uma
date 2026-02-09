class stackqueue:
    def __init__(self):
        self.stack_1=[]
        self.stack_2=[]
    def Enqueue(self,p):
            self.stack_1[len( self.stack_1):]=[p]
    def  Dequeue(self): 
        if len( self.stack_2)==0:
            while not len( self.stack_1)==0:
                  last= self.stack_1[len( self.stack_1)-1]
                  del self.stack_1[len( self.stack_1)-1]
                  self.stack_2[len( self.stack_2):]=[last]
        if len( self.stack_2)==0:
            print ("the queue iis empty")
            return
        v= self.stack_2[len( self.stack_2)-1]
        del self.stack_2[len( self.stack_2)-1]
        return v       
