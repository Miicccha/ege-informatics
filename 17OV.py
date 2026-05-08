arr=[]
f=open("1_17.txt")
for i in f:
    arr.append(int(i))
a=[]
m = 100000
for el in arr:
    if el>0 and el%123==0:
        m=min(el,m)

for i in range(0,len(arr)-1):
    if arr[i]+arr[i+1] <m:
        a.append(abs(arr[i]+arr[i+1]))
print(len(a),max(a))