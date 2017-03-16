T = input()
for t in range(T):
    noOfGame = input()
    merge = []
    for g in range(noOfGame):
        noOfpiles = input()
        stones = map(int, raw_input().split())
        for x in stones:
            merge.append(x)
            summ =0
    for m in merge:
        summ+=(m//2)
    if summ%2==0:
        print "Bob"
    else:
        print "Alice"
