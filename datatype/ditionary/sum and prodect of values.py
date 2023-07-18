d={"a":10,"b":20,"c":10}
s=0
p=1
x=d.values()
for i in x:
    s=s+i
    p=p*i
print(f"sum of values={s}")
print(f"product of values={p}")