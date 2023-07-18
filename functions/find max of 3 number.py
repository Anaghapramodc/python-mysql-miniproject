def max1(num):
    for i in range(len(num)):
        # print("i=",num[i])
        for j in range(len(num)):
            # print(j)
            if num[i]>=num[j]:
                num[i],num[j]=num[j],num[i]
                # print(num)
    print(num[0])
num=[3,6,5,4,15,1,29,11]
max1(num)
# def max(num):
