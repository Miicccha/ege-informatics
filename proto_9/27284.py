f = open('proto_9/27284.txt')
cnt = 0

for line in f:
    arr = list(map(int, line.split()))  
    min_val = min(arr)
    
    if arr.count(min_val) in (2, 3):
        
        others = [x for x in arr if x != min_val]
        if len(others) != len(set(others)):
            continue
    
        unique = [x for x in arr if arr.count(x) == 1]      
        if len(unique) >= 2:
            min_u = min(unique)
            max_u = max(unique)
            
            if min_u + max_u > sum(unique) - min_u - max_u:
                cnt += 1

print(cnt)