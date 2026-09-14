#Dictionary: Unordered key-value pairs
dictionary = {
    'a':True,
    'b':"Hello",
    'x':[1,2,3]
}

# print(dictionary['x'][1])

#A key in a dictionary should be immutable
#A key should be unique

dictionary = {
    123:True,
    False:"Hello",
    'x':[1,2,3]
}

print(dictionary)

#Dictionary methods
user = {
    'basket':[1,2,3],
    'greet':"Hello",
    'age':21
}

print(user.get('age'))
print(user.get('age', 55))

user2 = dict(name = 'Indra')
print(user2)

print('basket' in user.values())
print(user.items())#This is a tiple notation
# user.clear()
# print(user)
# user2 = user.copy()
# print(user.clear())
# print(user2)
# print(user.pop('age'))
# print(user)
# print(user.popitem()) This will remove the last inserted key value pair
print(user.update({'inventory':['Smartphone','Notebook','pen','Wallet']}))
print(user)