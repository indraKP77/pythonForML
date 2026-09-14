print(bin(5))
print(int('0b101',2))

#Escape sequence

weather = "It's \"kind of\" sunny \nhave a good day"
print(weather)

#Formatted Strings
name = 'Johnny'
age = 21
#print('hi' + name+ '.')
print(f'hi {name}. You are {age} years old.')

#String indexes / String slicing
print(name[0])
#[start:stop]
print(name[0:2])
#[start:stop:stepover]
print(name[0:6:2])
#[start:]
print(name[0:])
#[::-1]
print(name[::-1])

#Immutability
# can do this : name = "Indra"
# can't do this : name[0] = '1'

#Built in functions
print(len(name))
quote = "to be or not to be"
print(quote.upper())
print(quote.capitalize())
print(quote.lower())
print(quote.find('be'))
print(quote.replace('be','me'))

#booleans
isCool = False
print(isCool)
print(bool('True'))
print(bool(1))

#Exercise
name = 'Indra Kumar'
#birth_year = int(input('What year were you born'))
#age = 2026-birth_year
#print(f"You were born in the year {birth_year}")
#print(f"You are {age} years old")

#Exercise: Password checker
username = input("Enter your username ")
password = input("Enter your password ")
print(f"Hello {username}, your password {'*' * len(password)} is {len(password)} characters long")


