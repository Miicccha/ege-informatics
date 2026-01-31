n=0
def nto3 (n):
    s=''
    while n>0:
        s=str(n%3)+s
        n=n//3
    return s

def r(n):
    s=nto3(n)
    if n%3==0:
        s='1'+s+'21'
    else:
        s=s+nto3(n%3*5)
    return int(s,3)
for x in range(0,3000):
    if r(x)<=1130:
        print(x)