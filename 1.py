import math


def mod(a,b):
    if(a>b):
        return a-b
    else:
        return b-a


def distance(x1,y1,x2,y2):
    x=mod(x1,x2)
    y=mod(y1,y2)
    m=math.sqrt(x**2+y**2)
    return 'расстояние равно '+str(m)


print(distance(1,2,3,4))
