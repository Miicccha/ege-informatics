f=open('proto_17/17_23376.txt')
arr=[]
a=[]
for i in f:
    arr.append(int(i))
f.close()
m=-100000
for x in arr:
    if 10000<=abs(x)<=99999 and abs(x)%100==37:
        m=max(m,x)
cnt=0
for i in range(len(arr)-1):
    if(10000<=abs(arr[i])<=99999 and not(10000<=abs(arr[i+1])<=99999)) or (not(10000<=abs(arr[i])<=99999) and 10000<=abs(arr[i+1])<=99999):
        if ((arr[i]+arr[i+1])**2>m**2):
            a.append(arr[i]+arr[i+1])
print(len(a), max(a))