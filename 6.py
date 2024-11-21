def rec(b):
    a=int(input())
    if(a==0):
        return b
    return str(rec(a))+str(b)
a=int(input())
rec(a)