#build-in modules
#Math
import math
print(math.floor(1.1))

from math import floor
print(floor(1.1))

#print(help(math))
print(math.gcd(34,56))
print(math.pi)
print(math.e)
print(math.factorial(5))

#decimal
import decimal
from decimal import Decimal
value1 = Decimal(3.5)
value2 = Decimal(2.3)
print(value1- value2) # float is not accurate
print(type(value1- value2))

#statistics module
import statistics
number = [1,2,5,8,1,9]
print(statistics.mean(number))
print(statistics.median(number))
print(statistics.median_low(number))

#deque - useful in queue or stack processing
from collections import deque
queue = deque(['one', 'two'])
queue.pop()
print(queue)

queue.append('Three')
queue.appendleft('minus one')
print(queue)

#date module
import datetime
today = datetime.datetime.today()
print(today) #2020-12-11 16:40:58.201787 - micro-sec
print(today.hour)
print(today.day)

print(today.date)
print(today.time)

date = datetime.datetime(2020,3,24) #2020-03-24 00:00:00
print(date)

date = datetime.datetime(2020,3,24,1,4,20,59) #2020-03-24 01:04:20.000059
print(date)

print(date + datetime.timedelta(days=90))
print(date + datetime.timedelta(weeks=3))
print(date + datetime.timedelta(hours=45))
