#square pattern
A=65
for i in range(0,5):
    for l in range(A+i,(A+i)+5):
        print(chr(l),end=" ")
    print()
    A=A+4
