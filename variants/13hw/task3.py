cnt=0
num=0
alph='12345678'
for s1 in alph:
    for s2 in alph:
        for s3 in alph:
            for s4 in alph:
                for s5 in alph:
                    for s6 in alph:
                        for s7 in alph:
                            for s8 in alph:
                                for s9 in alph:
                                    s=s1+s2+s3+s4+s5+s6+s7+s8+s9
                                    num+=1
                                    #print(s)
                                    if(s2!=s3 and s3!=s4 and s4!=s5 and s5!=s6 and s6!=s7 and s7!=s8 and s8!=s9 and s.count('9')<=3 and s.count('8')<=3 and s.count('7')<=3 and s.count('6')<=3 and s.count('5')<=3 and s.count('4')<=3 and s.count('3')<=3 and s.count('2')<=3 and s.count('1')<=3 and s.count('0')<=3):
                                        cnt+=1
                                        print(cnt, s)
print(cnt, s)