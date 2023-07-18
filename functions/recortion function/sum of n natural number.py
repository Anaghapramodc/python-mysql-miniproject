def sum(k):
    if k>0:
        r=k+sum(k-1)
        return r
    else:
        r=0
        return r
print(sum(5))