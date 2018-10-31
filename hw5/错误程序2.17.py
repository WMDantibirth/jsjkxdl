def FA(a, b, c):
    carry = (a and b) or (b and c) or (a and c)
    sum = (a and b and c) or (not a and not b and c) or(not a and b and not c) or (a and not b and not c)
    return carry, sum


def add_2(x, y, c=False):
    if len(x) == 0:
        return c, y
    if len(y) == 0:
        return c, x
    x1 = x[0:len(x) - 1]
    y1 = y[0:len(y) - 1]
    c1, s1 = FA(x[len(x)-1], y[len(y)-1], c)
    print(c1)
    print(s1)
    carry, S_list = add_2(x1, y1, c1)
    print(carry)
    print(S_list)
    return carry, S_list + [s1]


print(add_2(['1', '1'], ['1', '1', '1', '1']))

