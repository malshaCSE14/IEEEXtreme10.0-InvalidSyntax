import operator
from itertools import groupby
def remove_dupes(arg):
    # create generator of distinct characters, ignore grouper objects
    unique = [i[0] for i in groupby(arg)]
    return unique
def find_offsets(colorList, character):
    occurences = []
    for c in range(len(colorList)):
        if colorList[c]==character:
            occurences.append(c)
    return occurences


T = input()
for t in range(T):
    N  = input()
    colors = raw_input().split()
    b1 = []
    b2 = []
    samplecolors = set(colors)

    warningforBrush =[]


    # print colorDictionry
    # sorted_x = sorted(colorDictionry.items(), key=operator.itemgetter(1))
    # print sorted_x


    kkkk =    remove_dupes(colors)
    colorDictionry = {}
    for cc in samplecolors:
        colorDictionry[cc] = 0
    for c in samplecolors:
        colorDictionry[c] = find_offsets(kkkk, c)
    # print colorDictionry
    # print kkkk
    for n in range(len(kkkk)):
        if n==0:
            b1.append(kkkk[0])
        elif n==1:
            b2.append(kkkk[1])
        elif kkkk[n]==b1[-1]:
            # print "oass"
            pass
        elif kkkk[n]==b2[-1]:
            pass
        else:
            b1future = []
            b2future = []

            for index in colorDictionry[b1[-1]]:
                if index>n:
                    b1future.append(index)
                    break
            for index in colorDictionry[b2[-1]]:
                if index>n:
                    b2future.append(index)
                    break
            b1future.sort()
            b2future.sort()
            # print b1future, b2future, "b1future,b2future"
            if len(b1future)==0:
                b1.append(kkkk[n])
                # break
            elif len(b2future)==0:
                b2.append(kkkk[n])
                # break
            else:
                if int(b1future[0])<int(b2future[0]):
                    # print "b1future is shorter than b2's. hence keep this appendkkkkn to b2 and go",kkkk[n]
                    b2.append(kkkk[n])
                    # print b2,"b2"
                    # break
                else:
                    b1.append(kkkk[n])
                    # break


    print len(b1)+len(b2)