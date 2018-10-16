n = input('请输入数：')
r = int(input('请输入R：'))
l = len(n)
k = 0
weight = r**(l-1)
for each in n:
    k += int(each)*weight
    weight //= r
print(k)
