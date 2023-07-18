def multi(k,m):
    if m>k:
        r=m+multi(k,m-1)
        print(r)
        return r
    else:
        return k
print(multi(5,10))