def fun1(a):    # 十进制转二进制
    x = int(a)
    Rs = []
    while x:
        r = x % 2
        x //= 2
        Rs = [r] + Rs
    return Rs


def bin2dec(b):     # 二进制小数部分转十进制
    d = 0
    k = 0.5
    for i in range(len(b)):
        if b[i] == '1':
            d += k
        k /= 2
    return d


def fun2(a):
    a = float('0.' + a)
    k = []
    x = 0.5
    while a != 0:
        if a >= x:
            k = k + [1]
            a = a - x
        else:
            k = k + [0]
        x /= 2
    return k


def fun3(b):
    x, y = b.split('.')
    x = fun1(x)
    y = fun2(y)
    return x, y


def dec2flost(x):
    ans = [0]*32
    if float(x) < 0:
        ans[0] = 1
        x = x[1:]
    if float(x) == 0:
        return '0'*32
    if '.' in x:
        spp = x
    else:
        spp = str(float(x))
    q0, q1 = fun3(spp)
    if q0:
        q2 = len(q0) - 1
        if q2 > 127:
            return '溢出'
        else:
            p1 = bin(q2+127)[2:][::-1]
            for i in range(len(p1)):
                ans[8 - i] = int(p1[i])
            q3 = q0[1:][::-1]
            for each in q3:
                q1 = [each] + q1
    else:
        k = 1
        while q1[0] == 0:
            k += 1
            q1 = q1[1:]
        q1 = q1[1:]
        if k > 126:
            return '0'*32
        jkl = fun1(-k+127)
        while len(jkl) < 8:
            jkl = [0] + jkl
        t = jkl[::-1]
        for i in range(len(t)):
            ans[8 - i] = int(t[i])
    if len(q1) < 23:
        omg = len(q1)
    else:
        omg = 23
    for i in range(omg):
        ans[9+i] = q1[i]
    fnc = ''
    for i in ans:
        fnc = fnc + str(i)
    return fnc


def float2dec(x):
    if x == '0'*32:
        return 0
    else:
        k = 1
        if x[0] == '1':
            k = -1
        p0 = x[1:9]
        p0 = int(p0, 2) - 127   # 指数
        p1 = x[9:]
        p2 = '1'
        if 0 < p0:
            while p0 != 0 and p1 != '':
                p2 = p2 + p1[0]
                p1 = p1[1:]
                p0 -= 1
            p1 = bin2dec(p1)
            t = (int(p2, 2) + p1)*2**p0
        elif p0 < 0:
            while p0 != -1:
                p2 = '0' + p2
                p0 += 1
            p2 = p2 + p1
            p2 = bin2dec(p2)
            t = p2
        else:
            p3 = bin2dec(p1)
            t = 1 + p3
        return t * k


x = dec2flost(input())
print(x)
if x != '溢出':
    print(float2dec(x))
