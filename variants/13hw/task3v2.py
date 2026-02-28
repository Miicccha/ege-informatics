cnt=0
alph='12345678'

for s1 in alph:
    for s2 in alph:
        if int(s1)%2 == int(s2)%2: continue
        for s3 in alph:
            if int(s2)%2 == int(s3)%2: continue
            for s4 in alph:
                if int(s3)%2 == int(s4)%2: continue
                for s5 in alph:
                    if int(s4)%2 == int(s5)%2: continue
                    for s6 in alph:
                        if int(s5)%2 == int(s6)%2: continue
                        for s7 in alph:
                            if int(s6)%2 == int(s7)%2: continue
                            for s8 in alph:
                                if int(s7)%2 == int(s8)%2: continue
                                for s9 in alph:
                                    if int(s8)%2 == int(s9)%2: continue
                                    s=s1+s2+s3+s4+s5+s6+s7+s8+s9
                                    ok = True
                                    for d in alph:
                                        if s.count(d) > 3:
                                            ok = False
                                            break
                                    if ok:
                                        cnt+=1
print(cnt)