n = 101101
p = str(n)
i = 0
weight = 2**(len(p)-1)
for s in range(len(p)):
    if int(p[s]):
        i += weight
    weight //= 2
print(i)
