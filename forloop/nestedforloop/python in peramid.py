word=input("enter the word")
char=len(word)
for i in range(char+1):
    for j in range(i):
        print(word[j],end="")
    print()