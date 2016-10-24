x,y,z = map(int, raw_input().split())
a= ((2*z)-(4*x)+y)/4
b= ((2*z)-y)/4
c = ((4*x)-(2*z)+y)/4
if a!=a//1 or a<0:
    print "Error"
elif b!=b//1 or b<0:
    print "Error"
elif c!=c//1 or c<0:
    print "Error"
else:
    print a,b,c
