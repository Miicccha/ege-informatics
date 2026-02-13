max_x =-1
result =0

for x in range(15):
    num1= int(f"99658{x}29",15)
    num2= int(f"102{x}023",15)

    total = num1 + num2
    if total %14==0:
        max_x=x
        result=total//14
print(max_x,result)