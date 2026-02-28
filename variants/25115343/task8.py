alph='акот'
cnt=0
for s1 in alph:
    for s2 in alph:
        for s3 in alph:
            for s4 in alph:
                s=s1+s2+s3+s4
                cnt +=1
                if (s1 != s2 and s2 != s3 and s3 != s4) and s.count('а') == 2:
                    print(s,cnt)