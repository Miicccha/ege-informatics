import sys 
import functools 

def to_base(n, base):
    s = ''
    while n > 0:
        s = str(n % base) + s
        n //= base
    return s


x = 5**100 + 3**50
s = to_base(x, 7)

print(s)
print(s.count('6'))
