def R(N):
    b = bin(N)[2:]
    if N%3==0:
        b = b+b[-3:]
    else:
        k =(N%3)*3
        b=b+bin(k)[2:]
    return int(b,2)

for N in range(1,100):
    if R(N) >= 76:
        print(N, R(N))
        break