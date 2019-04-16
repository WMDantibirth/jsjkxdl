def f(n):
    L = [1,2,3]
    P = [1,1,0]
    for i in range(3,n):
        L.append(L[len(L)-1]+L[len(L)-2]+L[len(L)-3]+P[i%3])
    return L

L = f(60)
for i in range(19,60):
    print(L[i])
