d={1:2,3:4}
x=int(input("Enter the elements to add: "))
for i in range(x):
    k=input("Enter the key: ")
    v=input("Enter the value: ")
    d[k]=v
print(d)       # {1: 2, 3: 4, '5': '6'}
