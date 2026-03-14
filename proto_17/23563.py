f=open('proto_17/17_23563.txt')
arr=[]
for i in f:
    arr.append(int(i))
f.close()
a=[]
m=100000

for x in arr:
    if x>0 and x%35==0:
        m=min(m,x)

for i in range(len(arr)-1):
    if arr[i]!=arr[i+1]:
        if abs(arr[i]-arr[i+1])%m==0:
            a.append(arr[i]+arr[i+1])
print(len(a),min(a))