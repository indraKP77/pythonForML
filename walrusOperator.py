#Walrus Operator
a = 'hello indra'

if ((n := len(a))>10):
    print(f"too long {n} elements")


#Scope - what variables do I have access to?

#1 - start with local
#2 - Parent local?
#3 - Global
#4 - built in python functions.

total = 0

def count():
    global total
    total += 1
    return total

count()
count()
count()
print(count())