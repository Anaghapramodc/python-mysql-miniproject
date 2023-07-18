def ssort(a):
    l = len(a)
    for i in range(l- 1):
        m = i
        for j in range(i + 1, l):
            if a[j] < a[i]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a
a = [21, 6, 9, 33, 3]
print("The sorted array is: ", ssort(a))