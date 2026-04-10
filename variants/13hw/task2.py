alph='вулорф'
cnt=0
for s1 in alph:
    for s2 in alph:
        for s3 in alph:
            for s4 in alph:
                for s5 in alph:
                    for s6 in alph:
                        for s7 in alph:
                            for s8 in alph:
                                s=s1+s2+s3+s4+s5+s6+s7+s8
                                cnt +=1
                                if s.count('о')==1:
                                    print(s,cnt)