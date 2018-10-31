def plus(p, q):  # 加法
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


def fun(a):  # 转码
    L = []
    for each in a:
        L.append(each)
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
    p = ''
    for each in L:
        p = p + each
    return p


def fun2(s, p):    # 转十进制
    if len(s) > 12:
        return 9999
    elif p and s[0] == '0':
        return 9999
    elif (not p) and s[0] == '1':
        return 9999
    else:
        r = int(s, 2)
        if r >= 2048:
            return r - 4096
        else:
            return r


def fun1(a):    # 十进制转二进制
    x = int(a)
    r = 0
    Rs = []
    while x:
        r = x % 2
        x //= 2
        Rs = [r] + Rs
    ans = ''
    for i in range(len(Rs)):
        ans = ans + str(Rs[i])
    return ans


def fun3(x, y):     # 乘法
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
    for i in range(len(b)):
        if b[len(b) - i - 1] == '1':
            lll = a + ['0'] * i
            L = plus(L, lll)
    ans = ''
    for each in L:
        ans = ans + each
    while len(ans) <= 11:
        ans = '0' + ans
    return ans


def mult(x, y, p):
    ans = fun3(x, y)
    if p:
        ans = fun(ans)
    return fun2(ans, p)


a = int(input())
b = int(input())
if -2048 <= a <= 2047 and -2048 <= b <= 2047:
    p = 0
    if a < 0 and b < 0:
        a = -a
        b = -b
    elif b < 0 < a:
        p = 1
        b = -b
    elif a < 0 < b:
        p = 1
        a = -a
    x = fun1(a)
    y = fun1(b)
    q = mult(x, y, p)
    if q == 9999:
        print('溢出错误')
    else:
        print(q)
else:
    print('溢出错误')
