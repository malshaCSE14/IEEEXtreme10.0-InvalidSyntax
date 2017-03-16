T = input()
for t in range(T):
    P,S,N = map(int, raw_input().split())
    memoryAddresses =[]
    for n in range(N):
        memoryAddresses.append(input())
    pageRequests=[]
    for  address in memoryAddresses:
        pageNo = address//S
        pageRequests.append(pageNo)
    osPage ={}
    recentlyUsed = []
    for  n in range(N):
        key = "osPage"+str(n)
        osPage[key] = []


