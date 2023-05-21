#Program to multiply a no. to all the items in a given dictionary
d={1: 2, 3: 4, 5: 6, 7: 8}
n=int(input("Enter a no. to multiply: "))
for i,j in d.items():
    i=i*n
    j=j*n
print(d)