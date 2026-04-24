cnt = 0

for s1 in range(1, 7):  # первая цифра не 0
    for s2 in range(0, 7):
        for s3 in range(0, 7):
            for s4 in range(0, 7):
                for s5 in range(0, 7):
                    s = str(s1) + str(s2) + str(s3) + str(s4) + str(s5)
                    
                    if s.count('0') == 1 and s.count('1') <= 2:
                        cnt += 1
print(cnt)