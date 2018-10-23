def fun(L):  # 转码
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


def fun2(s):    # 转十进制
    r = int(s, 2)
    if r >= 128:
        return r-256
    else:
        return r


x = int(input())
y = int(input())
a = 0
if x < 0:
    a = 1
    x = -x
i = 128
k = []
while i >= 1:
    if x // i:
        k.append('1')
        x = x - i
    else:
        k.append('0')
    i //= 2
if a:
    k = fun(k)  # k为x

b = 0
if y < 0:
    b = 1
    y = -y
i = 128
s = []
while i >= 1:
    if y // i:
        s.append('1')
        y = y - i
    else:
        s.append('0')
    i //= 2
if b:
    s = fun(s)  # s为y

ans = ''  # 开始加法
a = 0
for i in range(7, -1, -1):
    if int(k[i]) and int(s[i]):
        if a:
            ans = '1' + ans
        else:
            ans = '0' + ans
            a = 1
    elif not int(k[i]) and not int(s[i]):
        if a:
            ans = '1' + ans
            a = 0
        else:
            ans = '0' + ans
    else:
        if a:
            ans = '0' + ans
            a = 1
        else:
            ans = '1' + ans
if a and b:
    if not ans[0]:
        print('overflow')
    else:
        print(fun2(ans))
elif not a and not b:
    if ans[0]:
        print('overflow')
    else:
        print(fun2(ans))
else:
    print(fun2(ans))
