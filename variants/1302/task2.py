
def r(n):
    b=bin(n)[2:]

    if n%3==0:
        b=b+b[-3:]
    else:
        r=(n%3)*3
        b=b+bin(r)[2:]
    return int(b,2)
for n in range(1,1000):
    if r(n) >=76:
        print(n)
        break
