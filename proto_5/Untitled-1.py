def totree (n):
    s=''
    while n>0:
        s=str(n%3)+s
        n=n//3
    return s
def R(n):
    s=totree(n)
    if n%3==0:
        s='1'+s+'02'
    else:
        s= s+ totree((n%3)*5)
    return int(s,3)
for i in range(1,50):
    if R(i)>=177:
        print(R(i),i)
        break