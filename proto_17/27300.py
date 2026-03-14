f=open('proto_17/17_27300.txt')
arr=[]
for i in f:
    arr.append(int(i))
f.close()
a=[]
m=-100000

for x in arr:
    if (x)%100==11:
        m=max(m,x)

for i in range(len(arr)-2):
    if arr[i]>0 and arr[i+1]>0 and arr[i+2]>0:
        if arr[i]+arr[i+1]+arr[i+2]>m:
            a.append(arr[i]+arr[i+1]+arr[i+2])
print(len(a),min(a))