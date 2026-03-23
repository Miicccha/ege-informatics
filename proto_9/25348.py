f = open('proto_9/25348.txt')
cnt = 0

for line in f:
    arr = list(map(int, line.split()))
    if 3 in [arr.count(x) for x in set(arr)]:
        if len(set(arr)) == 5:
            if arr.count(max(arr)) == 1:
                cnt += 1

print(cnt)