from math import sqrt
cnt=0
n=8996452
def tre(num):
    return str(num).count('3')==2

def is_prime(x):
    for i in range(2,int(sqrt(x))):
        if x%i==0:
            return False
    return True

def x(sqt):
    for i in range(2,int(sqrt(sqt))):
        if sqt%i==0 and is_prime(i) and is_prime(sqt//i) and tre(i) and tre(sqt//i):
            return sqt//i
    return 0

while cnt !=5:
    n +=1 
    a=x(n)
    if a!=0:
        print(n,a)
        cnt+=1
