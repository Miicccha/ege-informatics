f=open('proto_17/17_23276.txt')
arr=[]
for i in f:
    arr.append(int(i))
f.close()
a=[]
m=-100000

for x in arr:
    if x%100==25:
        m=max(m,x)
for i in range(len(arr)-2):
    a1=arr[i]
    a2=arr[i+1]
    a3=arr[i+2]
    k=0
    for x in [a1,a2,a3]:
        if 1000<=abs(x)<=9999:
            k+=1
    if k<=2:
        s=a1+a2+a3
        if s<=m:
            a.append(s)
print(len(a), max(a))