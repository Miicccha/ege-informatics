f=open('proto_17/17_25356.txt')
arr=[]
for i in f:
    arr.append(int(i))
f.close()
a=[]
m=-100000
cnt=0


for x in arr:
    if abs(x)%100==30:
        m=max(m,x)

for i in range(len(arr)-2):
    if (not(1000<=arr[i]<=9999) and not(1000<=arr[i+1]<=9999) and not(1000<=arr[i+2]<=9999)):
        if arr[i]+arr[i+1]+arr[i+2]>m:
            a.append(arr[i]+arr[i+1]+arr[i+2])
            
print(len(a), max(a))