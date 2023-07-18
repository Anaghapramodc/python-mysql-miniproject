def num(num):
    def max1():
        for i in range(len(num)):
            for j in range(len(num)):
                if num[i] >= num[j]:
                    num[i], num[j] = num[j], num[i]
        num2=set(num)
        return num[1]
    return max1()
N=[7,12,88,88,12]
print(f"large number={num(N)}")

