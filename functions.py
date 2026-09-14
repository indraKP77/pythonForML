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

def sum(num1, num2):
    return num1+num2

print(sum(7,2))

#Docstrings
def test(a):
    '''
    Info: This functions prints a paramter
    '''
    print(a)

test('a')
help(test)
print(test.__doc__)