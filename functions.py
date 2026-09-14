#Functions
#parameters
#Default parameters
def sayHello(name = 'Darth Vader', emoji = '😈'):
    print(f'hello {name} {emoji}')

# positional arguments
sayHello('Indra','🔥')

#keyword arguments
sayHello(emoji = '🔥', name = 'Kumar')

sayHello()
sayHello('Moana')

# def sum(num1, num2):
#     return num1+num2

# print(sum(7,2))

#Docstrings
def test(a):
    '''
    Info: This functions prints a paramter
    '''
    print(a)

test('a')
help(test)
print(test.__doc__)

#*args **kwargs
#Rule: params, *args, default parameters, **kwargs

def superFunc(*args, **kwargs):
    total = 0
    print(*args)
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(superFunc(1,2,3,4,5, num1 = 5, num2 = 10))

def highestEven(li):
    highestEven = 0
    for i in li:
        if i%2 == 0:
            if i>highestEven:
                highestEven = i
    return highestEven

print(highestEven([1,2,3,4,8,9,10,11]))