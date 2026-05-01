def win(s1,s2):
    return s1+4+s2>=154 or s1*3+s2>=154 or s1+s2*3>=154
def lose1(s1,s2):
    return not(win(s1,s2)) and (win(s1+4,s2) and win(s1*3,s2) and win(s1,s2+4) and win(s1,s2*3))

def win1(s1,s2):
    return not(win(s1,s2)) and (lose1(s1+4,s2) or lose1(s1*3,s2) or lose1(s1,s2+4) or lose1(s1,s2*3))

def win2(s1,s2):
    return (win(s1+4,s2)or win1(s1+4,s2)) and \
          (win(s1*3,s2)or win1(s1*3,s2))and (win(s1,s2+4)or win1(s1,s2+4)) and (win(s1,s2*3)or win1(s1,s2*3)) and \
              not(win(s1+4,s2)and win1(s1,s2+4) and win(s1*3,s2)and win1(s1,s2*3) ) 

for s in range(1,143):
    if win2(11,s):
        print(s)

        

#19: 16 20:39,40 21:41