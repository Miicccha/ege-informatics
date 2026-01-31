x=((25**500)*(4*6+1)**(5**4)+7)//128
s=''
while x!=0:
    s=str(x%5)+s
    x=x//5
print(s.count('4'))