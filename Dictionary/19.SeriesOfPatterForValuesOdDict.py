from itertools import product
d={'1':['a','b'],'2':['c','d']}
for i,j in product(*d.values()):
    print(i+j)
    ''' ac
        ad
        bc
        bd'''