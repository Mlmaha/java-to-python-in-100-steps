#some sample errors in python
#print(1/0) #ZeroDivisionError
#print(2 + '2') #TypeError: unsupported operand type(s) for +: 'int' and 'str'
values = [1,'1']
#print(sum(values)) #TypeError: unsupported operand type(s) for +: 'int' and 'str'

#print(value) #NameError: name 'value' is not defined

#print(values.name) #AttributeError: 'list' object has no attribute 'name'

#to see all the built in exceptions
import builtins
#print(help(builtins))

try:
    i=0
    number = 10/i
except ZeroDivisionError: #catch
    number =0
except ValueError:
    number = 1

print(number)

#############

try:
    i=1
    number = 10/i
except (ZeroDivisionError, ValueError): #catch
    number =0
else: #executed only when exception is not thrown
    print('else')
finally: #always executed
    print('finally')

print(number)

class Amount:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def add(self, that):
        if(self.currency==that.currency):
            self.amount += that.amount
        else:
            #raise Exception('currency does not match')
            raise CurrencyDoNotMatchException(self.currency + " " + that.currency)

    def __repr__(self):
        return repr((self.currency,self.amount))

class CurrencyDoNotMatchException(Exception):
    def __init__(self, message):
        super().__init__(message)


amount1 = Amount('EUR',35)
amount2 = Amount('INR',70)

amount2.add(amount1)
print(amount2)
