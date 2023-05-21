#TAKING INPUT
d={}
x=int(input("Enter the size of dictionary:- "))
for i in range(x):
    k=eval(input("Enter the key:- "))
    v=eval(input("Enter the value:- "))
    d.update({k:v})
print(d)
#FIRST METHOD
y=sorted(d.values())
print(y)
