d={1:2,3:4}
d1={5:6}
d2={7:8}
res={}
for i in (d,d1,d2):
    res.update(i)
print(res)      #{1: 2, 3: 4, 5: 6, 7: 8}