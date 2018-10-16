n = input()
n = n.replace('0.', '')
print(n)
k = 0
p = 1/2
for each in n:
    k += int(each)*p
    p /= 2
print(k)
