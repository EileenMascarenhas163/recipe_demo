import math


x1=int(input("Enter x1:\n"))
y1=int(input("Enter y1:\n"))
x2=int(input("Enter x2:\n"))
y2=int(input("Enter y2:\n"))

dx = abs(x1-x2)
dy = abs(y1-y2)

if dx>dy:
    step= dx
else:
    step= dy

xinc = dx/step
yinc = dy/step


x=x1
y=y1
print("x=",x,"y=",y)


def pixel(x,y):
    print("x=",x,"y=",y)
    
    
while not (x == x2):
    x= x+xinc
    y=y+yinc
    pixel(math.trunc(x),math.trunc(y))
    #print (x,y)






