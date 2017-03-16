T = input()
for t in range(T):
    forwalker = []
    N,K = map(int, raw_input().split())
    dogsizes = []
    for n in range(N):
        dogsizes.append(input())
    dogsizes.sort(reverse=True)


    for d in dogsizes:
        forwalker.append([d])
    # print len(forwalker),"len(forwalker)",K,"K"
    while len(forwalker)>K:
        toBeNewSet = []
        indeces = []
        minDifference = dogsizes[0] - dogsizes[-1]
        duplicateforwalker = forwalker[:]
        for i in range(len(forwalker)-1):
            # print forwalker[i][-1]-forwalker[i+1][0],"forwalker[i][-1]-forwalker[i+1][0]"
            if (forwalker[i][-1]-forwalker[i+1][0]) < minDifference:
                minDifference=forwalker[i][-1]-forwalker[i+1][0]

                toBeNewSet = forwalker[i]+forwalker[i+1]
                indeces = [i,i+1]
        # print minDifference, "minDifference"
        # print indeces
        if (len(indeces)==2) & (len(forwalker)>1):
            forwalker = duplicateforwalker[:indeces[0]]
            forwalker+=[toBeNewSet]
            forwalker+= duplicateforwalker[indeces[1]+1:]
        # try:
        #     if len(duplicateforwalker[:indeces[0]])>0:
        #         forwalker = duplicateforwalker[:indeces[0]]
        # except IndexError:
        #     pass
        # forwalker+=[toBeNewSet]
        # try:
        #     if len(duplicateforwalker[indeces[1]+1:])>0:
        #         forwalker+=duplicateforwalker[indeces[1]+1:]
        # except IndexError:
        #     pass
        # print forwalker, "forwalker"
        sumz = 0
        for i in forwalker:
            i.sort()
            sumz+=i[-1]-i[0]
    print sumz
        # break