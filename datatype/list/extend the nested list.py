list1=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
sub_list=["h","i","j"]
list1[2][1][2].extend(sub_list)
print(list1)

#using insert
list1=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
sub_list=["h","i","j"]
list1[2][1][2].insert(2,sub_list)
print(list1)