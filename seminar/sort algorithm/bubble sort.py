def bSort(list1):
    for i in range(len(list1)-1,0,-1):
        for i in range(i):
            if list1[i]>list1[i+1]:
                temp = list1[i]
                list1[i] = list1[i+1]
                list1[i+1] = temp

list1 = [14,46,43,27,57,41,45,21,70]
bSort(list1)
print(list1)