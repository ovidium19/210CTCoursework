def CartesianP(sets,nr=0,pair=()):
    if nr==len(sets):
        print(pair)
    else:
        for i in range(len(sets[nr])):
            CartesianP(sets,nr+1,pair+(sets[nr][i],))
n=int(input("Nr of sets: "))
sets=[]
for i in range(n):
    sets.append([])
    lent=int(input("length of set: "))
    for j in range(lent):
        sets[i].append(int(input("Enter next element of set: ")))
CartesianP(sets)
