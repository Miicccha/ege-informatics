alph='аелпрь'
cnt=0
f=0
for s1 in alph:
    for s2 in alph:
        for s3 in alph:
            for s4 in alph:
                for s5 in alph:
                    for s6 in alph:
                        cnt+=1
                        s=s1+s2+s3+s4+s5+s6
                        if(s1!='а' and s1!='л' and s.count('п')>=2 and cnt%2==1):
                            f+=1
                            if f==1:
                                print(s,cnt)
                            break 
                            