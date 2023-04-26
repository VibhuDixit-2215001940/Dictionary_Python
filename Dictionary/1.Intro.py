#Dictionary-->It is the unordered collection of data used to store key and value pair.
#Keys must be unique.
#TAKING INPUT
d={}
x=int(input("Enter the size of dictionary:- "))
for i in range(x):
    k=eval(input("Enter the key:- "))
    v=eval(input("Enter the value:- "))
    d.update({k:v})
print(d)