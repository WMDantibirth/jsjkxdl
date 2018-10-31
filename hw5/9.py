def fun(x):
    p1 = int(x[0])
    p2 = int(x[1])
    p3 = int(x[2])

    x0 = not((not p1 and not p2 and p3) or (p1 and not p3))
    x1 = (not p1 and not p2 and not p3) or (p1 and not p2) or (p1 and not p3)
    x2 = not((p1 and not p2 and p3) or (p1 and p2 and not p3))
    x3 = not((not p1 and not p2) or (p1 and p2 and p3))
    x4 = (not p1 and not p3) or (p1 and p2 and not p3)
    x5 = p1 or not p2 or p3
    x6 = not((not p1 and not p2 and p3) or (p1 and not p2 and not p3) or (p1 and p2 and p3))
    print(x, end=' ')
    print('x0=%d,x1=%d,x2=%d,x3=%d,x4=%d,x5=%d,x6=%d' % (x0, x1, x2, x3, x4, x5, x6))


L = ('000', '001', '010', '011', '100', '101', '110', '111')
for i in L:
    fun(i)
