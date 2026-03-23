f=open('proto_9/27764.txt')
cnt=0
for i in f:
    arr=(list(map(int,(i.split('\t')))))
    if len(set(arr))==5 and 2*(max(arr)+min(arr)) == sum(arr)-(max(arr)+min(arr)):
        cnt+=1
print(cnt)