def fun1(L):  # 转码
    for i in range(len(L)):
        if L[i] == '1':
            L[i] = '0'
        else:
            L[i] = '1'
    k = 1
    for i in range(len(L)-1, -1, -1):
        if k and L[i] == '0':
            L[i] = '1'
            k = 0
        elif k and L[i] == '1':
            L[i] = '0'
    return L


def fun2(p, q):  # 加法
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
        else:
            p.append('0')
        p.reverse()
        return p


x = bin(int(input('被除数：')))[2:]
y = bin(int(input('除数：')))[2:]
L1 = []
L2 = []
for each in x:
    L1.append(each)
for each in y:
    L2.append(each)
i = 0
while 1:
    f = fun2(fun1(['0']*(len(L1)-len(L2)+1)+L2), ['0']+L1)
    g = 1
    for j in range(1, len(f)):
        if j == 1:
            g = 0
            break
    if len(L1) < len(L2) or f[1] == '1' or g:
        break
    a = len(L1)
    L1 = f
    if len(L1) > a:
        del(L1[0])
    while not int(L1[0]) and len(L1)-1:
        del(L1[0])
    i += 1
print('商：', end='')
print(i)
ans = ''
for each in L1:
    ans = ans + each
print('余数：', end='')
print(int(ans, 2))
