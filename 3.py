def capitalize(a):
    return chr(ord(a[0])-32)+a[1:]


qwe='hte qwe wqe qwe wqweqe sdkfdla asdd'
mas=qwe.split()
for elem in mas:
    print(capitalize(elem), end=' ')