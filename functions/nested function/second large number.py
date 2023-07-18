def num(num):
    def max1():
        for i in range(len(num)):
            for j in range(len(num)):
                if num[i] >= num[j]:
                    num[i], num[j] = num[j], num[i]
        print(num)
        for i in num:
            if num[0]==num[1]:
                num.remove(num[0])
            else:
                c=num[1]
        return c
    return max1()
N=[7,40,12,88,88,88,12]
print(f"second large number={num(N)}")