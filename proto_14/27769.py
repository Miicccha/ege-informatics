alph="0123456789ABCDEFGHIJKL"
def find(x):
    os=22
    xx=alph[x]
    s1=int(f"12313{xx}57",os)
    s2=int(f"1{xx}34561",os)
    return s1+s2
for x in range(22):
    if find(x)%21==0:
        print(x,find(x)//21)