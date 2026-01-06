def hanoi(x,start,middle,end):
    if (x==1):
        print (f"disk 1 changes {start} to {end}")
        return 
    else:
        hanoi(x-1,start,end,middle)
        print (f"disk: {x} cahnge  {start} to {end}")
        hanoi(x-1,middle,start,end)
        
x=int(input())
hanoi(x,"A","B","C")