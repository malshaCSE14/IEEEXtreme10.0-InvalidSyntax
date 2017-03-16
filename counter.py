def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False

    return True
lisssz = []
even = 0
n = input()

# for i in range(n/2,10,-2):
#     if isPrime2(n-i):
#         lisssz.append(n-i)
#         even  = i
#         break
ii = (n/2)+2
while ii>10:
    ii = ii-2
    if isPrime2(n-ii):
        lisssz.append(n-ii)
        even  = ii
        break

for ii in range(10,even):
    if isPrime2(even-ii)== True:
        # print even-ii, ii
        lisssz.append(even-ii)
        lisssz.append(ii)
        # print lisssz
        break
a=  map(str,lisssz)
try:
    print " ".join(a)
except:
    print "counterexample"

