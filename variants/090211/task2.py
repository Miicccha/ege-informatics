n = (16**8*4**20-4**5-64)
new_n=''
while n>0:
    new_n += str(n%4)
    n = n//4
print(new_n.count('3'))