f = open('proto_9/27285.txt')
cnt = 0

for i in f:
    arr = list(map(int, i.split('\t')))
    if all(arr[j] <= arr[j+1] for j in range(len(arr)-1)):
        
        even = sum(1 for x in arr if x % 2 == 0)
        odd = sum(1 for x in arr if x % 2 != 0)
        
        if even > odd:
            cnt += 1

print(cnt)