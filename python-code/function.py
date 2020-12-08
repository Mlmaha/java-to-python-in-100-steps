#python - structural and object oriented
#either single quotes or double quotes for string, no char type
print('hello world')

#indentaion - 4 tab - instead of braces in java
#function name - small case
def hello_world():
    print('hello')

#passing parameter - type not required for argument
def hello_world(times):
    #2 nd paramter in range is exclusive, so add +1
    for i in range (1,times+1):
        print('hello')

#hello_world(5)

def square_root(n):
    for i in range(1,n+1):
        print(i*i)

def square_root_even_numbers(n):
    for i in range(2,n+1,2):
        print(i*i)

def print_number_in_reverse(n):
    for i in range(n,0,-1):
        print(i)

def print_multiplication_table(table, start,end):
    for i in range(start,end):
        #formatted string
        print(f"{table} X {i} = {table *i}")


#method over-loading is not allowed Its achieved through default values
def print_multiplication_table1(table, start=1,end=10):
    for i in range(start,end):
        #formatted string
        print(f"{table} X {i} = {table *i}")

#return value from function
#returns None if no value is returned
def add_two_numbers(a,b):
    sum = a+b
    return sum

print(add_two_numbers(3,5))
