#Sets
# mlist = [1,2,3,4,5,5,3,7,0]
mset = {1,2,3,4,5,5}
# print(mset)
# mset.add(100)
# print(mset)
# print(set(mlist))
# print(1 in mset)
# print(list(mset))

#Set methods
yset = {3,4,5,6,7}
print(mset.difference(yset))
# print(mset.discard(5))
# print(mset)
# print(yset.difference_update(mset))
# print(yset)
print(mset.intersection(yset))# can also be done with &
print(mset.isdisjoint(yset))
print(mset.union(yset))# Can also be done with |
set1 = {3,4,5}
print(mset.issuperset(set1))
print(set1.issubset(mset))