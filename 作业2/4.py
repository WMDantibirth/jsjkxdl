n = 3
b = 2
p1 = 1
p2 = 1
for i in range(n+1):
    print(p1*p2)
    p1 = p1*(n-i)//(i+1)
    p2 *= b
