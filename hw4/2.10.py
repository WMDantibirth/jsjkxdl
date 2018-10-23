x = int(input('无符号整数：'))
y = int(input('位数：'))
p = bin(x)[2:]  # x的二进制数
if len(p) > y:
    print('False')
else:
    L = []
    L1 = []
    for i in p:
        L.append(i)
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
    ans = ''
    for each in L:
        ans += each
    print(ans)

