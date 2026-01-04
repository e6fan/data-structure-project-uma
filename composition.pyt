def composition(x):
    if(x==1):
        return 1
    else:
        return x*(composition(x-1))
n=4
r=2
m=composition(r)*composition(n-r)
comp=composition(n)/m
print(comp)

