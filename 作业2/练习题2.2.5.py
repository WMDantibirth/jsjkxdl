n = 'AA0C'
print('十进制%d' % int(n, 16))
p = bin(int(n, 16))[2:]
print('二进制%s' % p)
s = oct(int(n, 16))[2:]
print('八进制%s' % s)

