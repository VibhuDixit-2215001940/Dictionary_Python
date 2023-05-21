#Program to remove a user entered key pair
d={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, "Vibhu":36} 
k=int(input("Enter the key to remove: "))
for i in range(len(d)):
    if k in d:
        del d[k]
print(d)