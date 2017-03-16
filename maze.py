N = input()
def printer():
    return data
# def rebuilder1(colour, h1):
#     for i in range(1, len(colour)):
#         for h in range(height):
#             if h > h1:
#                 break
#             if colour[i] in data[h]:
#                 for w in range(width):
#
#                     if data[h][w] == colour[i]:
#                         data[h][w] = colour[0]

def pro1(h, w, colourNumber):
    colour = []
    if (w - 1) >= 0:
        if data[h][w - 1] > 1:
            colour.append(data[h][w - 1])
    if (w + 1) < N:
        if data[h][w + 1] > 1:
            colour.append(data[h][w + 1])
    if ((h - 1) >= 0):
        if data[h - 1][w] > 1:
            colour.append(data[h - 1][w])
    colour = list(set(colour))
    if len(colour) == 0:
        data[h][w] = colourNumber[0]
        colourNumber[0] += 1
    elif len(colour) == 1:
        data[h][w] = colour[0]
    # else:
    #     rebuilder1(colour, h)
    #     data[h][w] = colour[0]
openRooms1 = []
coordinate = raw_input()
while coordinate!="-1":
    openRooms1.append(map(int, coordinate.split()))
    coordinate = raw_input()
openR = []
data = []
for h in range(N):
    newline = []
    for i in range(N):
        newline.append(0)
    data.append(newline)

for i in range(len(openRooms1)):
    openRooms = openRooms1[:i]
    for r in openRooms:
        openR.append([r[0]-1,r[1]-1])
    for dd in openR:
        data[dd[0]][dd[1]]=1
    colourNumber1 = [2]
    for h in range(N):
        if (len(set(data[h])) == 1):
            if data[h][0] == 0:
                continue
        for w in range(N):
            if data[h][w] == 1:
                pro1(h, w, colourNumber1)
    a = printer()
    max = 0
    for j in a[-1]:
        if j>max:
            max = j
    win =False
    for zz in range(2,max+1):
        coordsfortheReigon = []
        for x in a[0]:
            if x==zz:
                for y in a[-1]:
                    if y==zz:
                        print len(openRooms)
                        win=True
                        break
            if win == True:
                break
    if win == True:
        break
if win==False:
    print "-1"
