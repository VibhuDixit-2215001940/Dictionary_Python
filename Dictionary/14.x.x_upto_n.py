#Program to made aa dictionary from 1 to n by multiplying x*x as value.
n=int(input("Enter the range: "))
d={}
for i in range(1,n+1):
    k=i
    v=i*i
    d[k]=v
print(d)        #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    