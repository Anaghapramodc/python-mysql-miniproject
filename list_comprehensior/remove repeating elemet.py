list1=['a','a','s','d','f','f']
newlist=[i for i in list1 if str(list1[list1.index(i)+1:]).find(i)==-1 or str(list1[list1.index(i)+1:]).find(i)==list1.index(i)]
print(newlist)
