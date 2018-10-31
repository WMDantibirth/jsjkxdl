def fun(n):
    a = int(n[0])
    b = int(n[1])
    c = int(n[2])
    x = (a & b & c) | (a & (~b) & (~c)) | ((~a) & b & (~c)) | ((~a) & (~b) & c)
    return x


L = ['000', '001', '010', '011', '100', '101', '110', '111']
for each in L:
    print(each[0], end=' ')
    print(each[1], end=' ')
    print(each[2], end=' ')
    print(fun(each))
