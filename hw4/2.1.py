def fun(p, d=0):
    if len(p) == 1:
        if p == '1':
            d += 1
        return d
    else:
        if p[0] == '1':
            d += 2**(len(p)-1)
        p = p[1:]
        return fun(p, d)


b = input('Please enter a binary number:')
print(fun(b))

