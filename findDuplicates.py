#Exercise
someList = ['a','b','c','b','d','m','n','n']

duplicates = []
for i in someList:
    if someList.count(i)>1:
        if i not in duplicates:
            duplicates.append(i)

print(duplicates)