for n in range(1,1000):
    b = bin(n)[2:]

    if n%3==0:
        b =b+b[-3:]
    else:
        r=(n%3)*3
        b=b+bin(r)[2:]
    r=int(b,2)
    if r>=200:
        print(n)
        break