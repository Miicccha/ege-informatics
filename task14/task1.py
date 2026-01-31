n=(((16**350)*((15*3 -29)**(4**7)))+1007)//63
new_n = ""
while n> 0:
    new_n+= str(n % 4)
    n = n // 4
print(new_n.count("1"))