from functools import partial

def s(x, y):
    return x * y

d = partial(s, y = 8)
print(d(9))