def to11(n):
    s=''
    while n>0:
        s=str(n%11)+s
        n//=11
    return s
num=0
for x in range(1,3001):
    s=9*11**210+8*11**150-x
    b=to11(s)
    if b.count('0')==60:
        num=x
print(num)