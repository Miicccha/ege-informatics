f=open('proto_9/27287.txt')
cnt=0
for i in f:
    arr=(list(map(int,(i.split('\t')))))
s=set(arr) 
a=[]
for el in s:
    #if len(s)==3:
        a.append(arr.count(el))
print(a)
    

#9_№ 27287 (Уровень: Базовый)
#9_№ 27285 (Уровень: Базовый)
#9_№ 27284 (Уровень: Средний)
#9_№ 25348 ЕГКР 13.12.25 (Уровень: Базовый)
#negrs :\