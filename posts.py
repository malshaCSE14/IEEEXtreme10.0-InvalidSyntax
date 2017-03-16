while True:
    try:
        A,P = map(int, raw_input().split())
        postNumbers =[]
        for p in range(P):
            postNumbers.append(input())
        # print postNumbers
        postDictionary = {}
        for n in range(P):
            if postNumbers[n]==0:
                postDictionary[n+1] = [n+1]

        # print postDictionary
        for postNo in range(len(postNumbers)):
            for eachKey in postDictionary:
                numberList = postDictionary[eachKey]
                if numberList[-1]==postNumbers[postNo]:
                    l = postDictionary[eachKey] + [postNo+1]
                    postDictionary[eachKey] = l
        # print postDictionary
        lengths = []
        for key in postDictionary:
            lengths.append(len(postDictionary[key]))
        # print lengths
        minSum = sum(lengths)
        for i in range(len(lengths),0,-1):
            if sum(lengths[:i])<=A:
                print A-sum(lengths[:i])
                break
            else:
                pass

    except:
        break


