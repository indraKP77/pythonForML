#Tuple
#Immutable list is a tuple
tup = (1,2,3,4,5)
print(tup)
newTup = tup[0:2]
print(newTup)
x,y,z, *other = tup
print(x)

#Tuple methods
print(tup.count(1))
print(tup.index(3))