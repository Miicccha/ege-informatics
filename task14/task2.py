n = ((25**500)*((4*6+1)**(5**4))+7)//128
new_n = ""
while n>0:
    new_n += str(n%5)
    n = n//5
print(new_n.count("4"))
