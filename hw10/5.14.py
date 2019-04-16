def f(n):
    L=[{'1'},{'11','2'},{'111','12','21'}]
    P=[1,2,3]
    for i in range(3,n):
        x = set();y = set(); z = set()
        x1= L[0];y1 = L[1];z1 = L[2]
        for i in x1:
            x.add(i[0]+'3'+i[1:])
            for j in range(len(i)):
                x.add(i[:j]+'3'+i[j:])
        for i in y1:
            y.add(i[0]+'2'+i[1:])
            for j in range(len(i)):
                y.add(i[:j]+'2'+i[j:])
        for i in z1:
            z.add(i[0]+'1'+i[1:])
            for j in range(len(i)):
                z.add(i[:j]+'1'+i[j:])
        k = set()
        for each in x:k.add(each)
        for each in y:k.add(each)
        for each in z:k.add(each)
        L.append(k)
        P.append(len(k))
        del(L[0])
    return P
    
print(f(25))
