#print keynames from a nested list
dict={"class":
    {
        "dict1":{"name":"anagha","age":22},
        "dict2":{"place":"kannur"},
        "dict3":{"course":"python","time":"9 am"}
    },
    "Home":
        {
            "dict4":{"address":"abcd"},
            "dict5":{"pin":670643}
        }
     }
x=dict.keys()
for i in x:
    print(i)
    for j in dict[i]:
        print(j)
        for k in dict[i][j]:
            print(k)
    print("\n")




