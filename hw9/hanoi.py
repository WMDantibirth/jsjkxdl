def hanoi(n,a,b,c):
    global L
    if n<1:print('False')
    elif n==1:
        L.append([a,c])
    elif n>1:
        hanoi(n-1,a,b,c)
        hanoi(1,a,c,b)
        hanoi(n-1,b,c,a)
        
L=[]
s = hanoi(4,'a','b','c')


