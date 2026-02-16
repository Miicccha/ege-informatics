for x in range(1,27001):
    a=(3*27**9)+(2*27**6)+(27**3)-x
    k=0
    while a !=0:
        if a%27==0: k+=1
        a=a//27
    if k==6:
        print(x)
        break