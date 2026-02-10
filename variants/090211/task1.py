aplh='еиортя'
cnt=0
for w1 in aplh:
    for w2 in aplh:
        for w3 in aplh:
            for w4 in aplh:
                for w5 in aplh:
                    for w6 in aplh:
                        cnt +=1
                        W=w1+w2+w3+w4+w5+w6
                        if (w1 != 'е' and w1 != 'и' and w1 != 'о' and W.count('я') == 1 and cnt % 2 == 0):
                            print(cnt, W) #7782
                            exit()