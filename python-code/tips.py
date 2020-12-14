#get index
numbers = [1,5,7]

for index, number in enumerate(numbers):
    print(f'{index}, {number}')

words = ['saraa', 'meena']

for index, string in enumerate(words):
    print(f'{index}, {string}')

##################
#enum

from enum import Enum

class Currency(Enum):
    USD =1
    EUR = 2
    INR = 3

#print(Currency.EUR)

for currency in Currency:
    print (currency)

print(Currency(1))
print(Currency(1).name)
print(Currency(1).value)

################
#method and arguments

def example(mandatory_argument, default_argument = 1, *args, **kwargs):
    print(f"""
    mandatory_argument = {mandatory_argument} {type(mandatory_argument)}
    default_argument = {default_argument} {type(default_argument)}
    args = {args} {type(args)}
    kwargs = {kwargs} {type(kwargs)}
    """)

#example() #TypeError: example() missing 1 required positional argument: 'mandatory_argument'
example(12) #positional paramter
example(mandatory_argument=12) #named paramter

example(12, 2)
example(12, 'maha')


example(12, 'maha', 'string1', 3, 5) #*args - any number of arguments

example(12, 'maha', 'string1', 3, 5, key1 ='a', key2 = 'b') #keyword arguments

example(key1 ='a', key2 = 'b', mandatory_argument =12, default_argument='maha') #different order with named args

example_list = [1,2,3,4]
example(*example_list)
example_dict = {'key1': 'a', 'key2': 'b'}

example(*example_list, **example_dict)

#None - similar to null, no-content/no-value

def email(content, subject, to, cc=None, bcc=None):
    print(f" {content}, {subject}, {to}", {cc}, {bcc})

email('subject', 'hello Maha', 'ma123@gmail.com')
email(None, 'hello Maha', 'ma123@gmail.com')

#str vs repr

import datetime

today = datetime.datetime.today()
print(today.__str__()) #2020-12-14 10:50:34.825665 - human readable form

print(today.__repr__()) #2020-12-14 10:50:34.825665

#switch - no switch - use dict

week_days = {
    0 : 'Sunday',
    1 : 'Monday',
    2 : 'Tuesday'
    # You can fill rest of the stuff
}

print(week_days.get(7,'Invalid_day')) #key and default value
print(week_days.get(1,'Invalid_day'))

#random
import random
print(random.random()) #random value from 0 to 1

print(random.randint(1,10)) #random integers - both are inclusive

print(random.randrange(1,25,2)) #random odd number

list = [1,25,14,32]
print(random.choice(list))
print(random.choice(list))
print(random.choice(list))

print(random.sample(list,2))#returns 2 random numbers from the list

print(random.choice('abcdefghijklmnopqrstuvwxyz'))

#return multiple values

def some_function():
    return 1, 'string', 4.5

tuple1 = some_function()
print(tuple1)

print(tuple1[0])
print(tuple1[1])

#named tuple
from collections import namedtuple
Point = namedtuple('Point', ['x','y'])

point = Point(1,2)
print(point.x)
print(point.y)

#3d point
threeDPoint = namedtuple('threeDPoint',['x','y','z'])
testpoint = threeDPoint(10,5,4)
print(testpoint.z)

#encapsulation
#no private variable/method
#no getters and setters
#property decorator
class BookEnhanced:
    def __init__(self, name, copies):
        self.name = name
        self._copies = copies #_ means protected field

    @property
    def copies(self):
        print('getter called')
        return self._copies

    @copies.setter
    def copies(self, copies):
        print('setter called')
        if(copies>=0):
            self._copies = copies

microservices = BookEnhanced('Microservices',5)

print(microservices.copies)

microservices.copies = 10

print(microservices.copies)

#operatoer overloading
#object compare
from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __add__(self, other):
        return Money(self.currency, self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.currency, self.amount - other.amount)

    def __repr__(self):
        return repr((self.currency, self.amount))

    def __eq__(self, other):
        return (self.currency, self.amount) == (other.currency,other.amount)

    def __le__(self, other):
        return (self.amount) <= (other.amount)

amount1 = Money('EUR', 10)
amount2 = Money('EUR', 20)
amount3 = Money('EUR', 10)

print(amount1 < amount2)
print(amount2 < amount3)
print(amount3 < amount1)

print(amount3 <= amount1)
print(amount3 >= amount1)

# print(amount1 == amount2)
# print(amount1 != amount2)
# print(amount1 == amount3)
# print(amount1 != amount3)

# print(amount1 + amount2)
# print(amount2 - amount1)



# object.__add__(self, other)
# object.__sub__(self, other)
# object.__mul__(self, other) *
# object.__matmul__(self, other)
# object.__truediv__(self, other) \
# object.__floordiv__(self, other) \\
# object.__mod__(self, other) %
# object.__pow__(self, other[, modulo]) **
# object.__and__(self, other) and
# object.__xor__(self, other) ^
# object.__or__(self, other) or
#
# i methods


