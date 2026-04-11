def r(n):
    s=bin(n)[2:]
    if n%2==0:
        s='10'+s
    else:
        s='1'+s+'01'
    return int(s,2)
for n in range(1,100):
    if(n>18):
        print(r(n),n)
