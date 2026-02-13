def DEL(n,m):
    return n%m==0
max_A = 0

for A in range(1,301):
    ok = True
    for x in range(1,1000):
        left =(not DEL(x,A))and DEL(x, 35)
        right =(not DEL(x,21))or (not DEL(x, 35))

        if left and not right:
            ok=False
            break
    if ok:
        max_A = A
print(max_A)