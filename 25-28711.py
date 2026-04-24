from math import sqrt
cnt=0
n=2400000
def tre(num):
    return str(num).count('4')>=1 or str(num).count('7')>=1

def is_prime(x):
    for i in range(2,int(sqrt(x))):
        if x%i==0:
            return False
    return True

def x(sqt):
    for i in range(2,int(sqrt(sqt))):
        if sqt%i==0 and is_prime(i):
            return i
    return 0
def xsqt(sqt):
    f=x(sqt)
    if f==0 or not tre(f):
        return 0
    res1=sqt//f
    s=x(res1)
    if s==0 or not tre(s): return 0
    res2=res1//s
    if is_prime(res2) and not tre(res2): return res2

    return 0
    

while cnt !=5:
    n +=1 
    a=xsqt(n)
    print(n,a)
    if a!=0:
        print(n,a)
        cnt+=1
