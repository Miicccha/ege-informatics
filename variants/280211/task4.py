alph='акорст'
cnt=0
for s1 in alph:
    for s2 in alph:
        for s3 in alph:
            for s4 in alph:
                for s5 in alph:
                    for s6 in alph:
                        s=s1+s2+s3+s4+s5+s6
                        if('а' not in s1 and 'с' not in s1 and 'т' not in s1) and (s.count('о')==2):
                            cnt+=1
                            #print(s,cnt)
                            if cnt%2==0:
                                print(s,cnt)