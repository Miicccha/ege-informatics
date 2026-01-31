P = list (range(25,65))
Q = list (range(40,116))
A = []

for x in range(0,150):
    if((x in P)<=((x in Q) or (x not in A)) <= (x not in P) ):
        A.append(x)
print(A)
print(len(A))