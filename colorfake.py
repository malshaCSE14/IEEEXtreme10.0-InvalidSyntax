T = input()
baloons = ['rgb']*10
for t in range(T):
    bDup = baloons[:]
    newline = raw_input()
    s1,s2 = map(int, raw_input().split())
    for s in range(s1):
        question = raw_input().split()
        answer = raw_input()
    if s1==s2:
        bDup[0] = "rg"
        bDup[1] = "r"
    elif (s2>0) & ((s1-s2)==2):
        bDup[0] = "b"
        bDup[1] ="r"
        bDup[2] ="b"
        bDup[3] ="g"
    print " ".join(bDup)


