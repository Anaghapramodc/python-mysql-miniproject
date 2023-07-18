#write a pp to generate random values in a string random numbers randum colours in hex random multiple btwn 0 to
import random
#random alphabetical string
print(random.randint(22,67))
print(random.randrange(0,71,7))

randm_clr=random.randint(0,16777215)#range of hex colours
s=str(hex(randm_clr))
print(s)
hex_num='#'+s[2:]
print("hex colour code is",hex_num)

s1="python"
s2=""
print(random.choice(s1))

