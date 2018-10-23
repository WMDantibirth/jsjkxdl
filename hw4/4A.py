def fun(p, q):
    if not len(p):
        return q
    else:
        p.reverse()
        q.reverse()
        a = 0
        for i in range(len(q)):
            if i+1 <= len(p) and a and int(p[i]) and not int(q[i]):
                p[i] = '0'
            elif i+1 <= len(p) and a and not int(p[i]) and not int(q[i]):
                p[i] = '1'
                a = 0
            elif i+1 <= len(p) and not a and int(p[i]) and int(q[i]):
                p[i] = '0'
                a = 1
            elif i+1 <= len(p) and not a and not int(p[i]) and int(q[i]):
                p[i] = '1'
            elif i+1 > len(p):
                if a and int(q[i]):
                    p.append('0')
                elif a:
                    p.append('1')
                    a = 0
                elif int(q[i]):
                    p.append('1')
                else:
                    p.append('0')
        if a:
            p.append('1')
        p.reverse()
        return p


x = bin(int(input()))[2:]
y = bin(int(input()))[2:]
L1 = [i for i in x]
L2 = [i for i in y]
a = len(L1)
b = len(L2)
if a > b:
    a = L1
    b = L2
else:
    a = L2
    b = L1  # a是大的，b是小的
L = []
k = 1
for i in range(len(b)):
    if b[len(b)-i-1] == '1':
        lll = a + ['0']*i
        L = fun(L, lll)
ans = ''
for each in L:
    ans = ans + each
print(int(ans, 2))


