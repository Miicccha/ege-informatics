cnt=0
x=[]
for r in range(3521,13019+1):  
        if(r%6==0 and r%15==0 and r%9>0 and r%12>0 and r%17>0 and r%21>0):
            x.append(r)
print(len(x), max(x))