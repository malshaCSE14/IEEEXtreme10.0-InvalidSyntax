T =input()
for t in range(T):
    P = input()
    mala = range(1,P+1)
    start = 0
    while len(mala)>1:
        remainList = []
        for e in range(start,len(mala),2):
            remainList.append(e)
        newMala = []
        for r in remainList:
            newMala.append(mala[r])
        lastMala = mala[-1]
        lastNewMala = newMala[-1]
        mala=newMala
        if lastMala==lastNewMala:
            start = 1
        else:
            start =0
    print mala[0]


