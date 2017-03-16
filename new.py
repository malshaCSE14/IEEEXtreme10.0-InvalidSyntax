
height  =width  =4

data = []


for h in range(height):
    newline = []
    for i in range(width):
        newline.append(0)
    data.append(newline)

# hh=0
ww=3
for dd in openR:
    data[dd[0]][dd[1]]=1
# data[hh][ww]=1



# _____________________________________________________________
# /////////////////////////////////////////////////////////////
def printer():
    print data
    for i in data:
        print ' '.join(map(str, i))
    print ""


# _____________________________________________________________
# /////////////////////////////////////////////////////////////
def rebuilder1(colour, h1):
    for i in range(1, len(colour)):
        for h in range(height):
            if h > h1:
                break
            if colour[i] in data[h]:
                for w in range(width):

                    if data[h][w] == colour[i]:
                        data[h][w] = colour[0]


# _____________________________________________________________
# /////////////////////////////////////////////////////////////
def pro1(h, w, colourNumber):
    colour = []
    if (w - 1) >= 0:
        if data[h][w - 1] > 1:
            colour.append(data[h][w - 1])
    if (w + 1) < width:
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
    else:
        rebuilder1(colour, h)
        data[h][w] = colour[0]


colourNumber1 = [2]
for h in range(height):
    if (len(set(data[h])) == 1):
        if data[h][0] == 0:
            continue

    for w in range(width):
        if data[h][w] == 1:
            # print "call pro1"
            pro1(h, w, colourNumber1)
printer()
