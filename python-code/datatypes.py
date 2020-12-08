#numbers - int, float
#everything is treated as python objects, no primitives
#no need to mention type as int. It is inferred from the given value
print("********* number operations start************")
print(type(12345))
print(type(12345.23))

#division always results in float
print(type(5/3))
#use // if interger result is required for division
print(type(5//3))

#power
print(4 ** 5)
print(pow(4,5))

#number operations - ++ and -- is not allowed
number = 10
number = number +1
number += 1 #shorthand operator

#max and min
print(max(2,4,3))
print(min(8,9,7))

#round
print(round(5.6))
print(round(5.2))

#number conversion
print(int(5.6)) #int to float
print(float(5)) #float to int

print("********* number operations end************")


print("***************boolean start *****************")
#bool - True & False - first letter should be in caps
print(type(True))
print(type(False))

#boolean operators - and or not ^
#short-circuit operation - and or, the second values are not evealuted
print(True and False)
print(True or False)
print(not(True))
print(True^False) #xor
print(True^True)
print("***************boolean end *****************")


print("************ strings ***********************")
#str - single or double quotes, no char
print(type('c'))
print(type('cba'))

string="hello"
print(string.upper())
print(string.lower())
print(string.capitalize())
print("hello".capitalize())

print(string.islower())
print(string.isupper())
print(string.istitle()) #checks the first letter - caps

print("**************")
print('123'.isdigit())
print('A23'.isdigit())
print('avc'.isdigit())
print('avc'.isalpha())
print(string.isalnum()) #checks alpha-numeric

print('Hello World'.endswith('ld'))
print('Hello World'.startswith('Hel'))
#find - returns the matching position of the first letter, returns -1 if there is no match
print('Hello World'.find('Hello')) #returns 0 - starting position
print('Hello World'.find('ello')) #retruns 1
print('Hello World'.find('ab')) #returns -1 if not exists
print('Hello World'.find('bello'))

#string conversion
print("**************")
print(str(True)) #bool to string
#string to bool
print(bool('True')) #returns true if there is any content
print(bool('xxx'))
print(bool('Fal'))
print(bool('')) ##returns false if there no content
#int to str
print(str(123))
print(str(456.23))
print(type(str(456.23)))

#str to int
print(int('45'))
#throws error for int('45.6') int('45fabc')
print(int('45abc',16)) #base-16 hexadecimal
print(int('b',16)) #returns hexa-decimal equiualent of a

print(float('13.35')) #string to float

#immutable - str, bool, int, float
string = "hello"
string.upper() #this creates a new string and original string is unaffected
string = string.upper() #object reference is changed

#char
message = "Hello World"
print(message[0]) #returns first char
##print(message[100]) #returns error index out of range
print(type(message[0])) #returns str class - there no char type in python
for ch in message:
    print(ch)

#string module
import string
print(string.ascii_letters)
print(string.punctuation)
print('a' in string.ascii_letters) #returns true, in checks for sub-set

#vowel
vowel_pattern = 'AEIOUaeiou'
print('A' in vowel_pattern) #true
print('w' in vowel_pattern) #false

#prints all the ascii letters
for char in string.ascii_lowercase:
    print(char)
print("************ strings ***********************")


#dynamic typing - same variable can be assigned to diff values/data-types
str = 123
print(type(str))

str = "hi hello"
print(type(str))

str = [1,2,3]
print(type(str))

print("******* excersie **********")
#exercise - split a sentence to words
sentence = 'This is wonderful'
for word in sentence.split():
    print(word)
#split lines - based on \n
sentence = 'This\nis\nwonderful'
for word in sentence.splitlines():
    print(word)

#concatenation
print('1'+'2') #both should be same type
#print('1'+2) #throws error, becaz of different type
print('1' *20) #repeats 1, 20 times
print('A' *20)
