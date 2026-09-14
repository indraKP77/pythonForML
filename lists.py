#Lists: Ordered sequence of objects of any type
li = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2,'a',True, 2.5]

#print(li3[3])

#List slicing

# amazon_cart = [
#     'notebook',
#     'sunglasses',
#     'toys',
#     'grapes'
# ]

# print(amazon_cart)
# print(amazon_cart[0:2])
# print(amazon_cart[0::2])


#Lists are mutable
# amazon_cart[0] = 'laptop'
# print(amazon_cart)
# newCart = amazon_cart[:]
# newCart[0] = 'gum'
# print(newCart)
# print(amazon_cart)

#List Methods
#All these methods work in place except pop, clear
basket = [1,2,3,4,5]
#adding
# basket.append(100)
# newList = basket
# print(newList)
# print(len(basket))

#insert
# basket.insert(4,100)
# print(newList)

#remove
# basket.pop()
# print(basket)
# basket.pop(4)
# print(basket)
# basket.clear()
# print(basket)
# print(newList)

basket = ['a','x','b','c','d','e','d']
# print(basket.index('b'))
#print(basket.index('d',0,4))
# print('d' in basket)
# print('i' in "I an in India")
# print(basket.count('d'))

# basket.sort()
# basket.append('x')
# newBasket = basket.copy()
# newBasket.sort()
# print(sorted(newBasket))
# print(sorted(basket))
# print(basket)

#reverse
# basket.sort()
# basket.reverse()
# print(basket)

#Common list patterns

# print(basket[::-1])
# print(basket)
# print(list(range(101)))

# sentence = '1'
# newSentence = sentence.join(['hi','my','name','is','JOJO'])
newSentence = ' '.join(['hi','my','name','is','JOJO'])
print(newSentence)

#List unpacking
# a,b,c = [1,2,3]

# print(a)
# print(b)
# print(c)

# a,b,c, *other,d = [1,2,3,4,5,6,7,8,9]

# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

#None

# a = None
# print(a)