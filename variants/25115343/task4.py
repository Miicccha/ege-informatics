for n in range(1,1000):
    b = bin(n)[2:]
    #print(b)
    if n%2==1:
        b = b[-1] + b[1:-1] + b[0]
        r = b + '1'
        #print(r)
    else:
        r = b + '0'
        #print(r)
    R = int(r,2)
    if R >= 50:
        print(n,R,r)
        break