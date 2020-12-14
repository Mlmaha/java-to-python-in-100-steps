from functools import reduce

def multiply_by_2(data):
    return data * 2

#function can be stored in a variable
func_example = multiply_by_2
print(func_example(23))

def do_this_and_print(func, data): #function can be passed as a parameter
    print(func(data))

do_this_and_print(multiply_by_2,4)

#lambda
do_this_and_print(lambda data:data*5,4) #anonymous function and input

do_this_and_print(lambda data:data*data,5) #square

#lambda - to invoke functions
do_this_and_print(lambda data:len(data),'Test') #square

#filter
number = [25,15,16,4]
filter(lambda x: x%2==1, number) #function - criteria and input to process
#this creates a filter object - to get odd numbers from the list

print(list(filter(lambda x: x%2==1, number))) #returns a odd number list
print(list(filter(lambda x: x%2==0, number))) #returns a even number list

print(list(filter(lambda x: x%2, number))) #return odd numbers - non-zero value is considered as true

words = ['saraa', 'meena','hellooo']
print(list(filter(lambda x: x.endswith('a'), words)))

print(list(filter(lambda x: len(x) == 5, words)))

#map - transformation - one to one mapping
print(list(map(lambda x: x.upper(), words)))
print(list(map(lambda x: len(x), words)))

print(list(map(lambda x: x*x, number)))
print(list(map(lambda x: x*x, range(1,11))))
print(list(map(lambda x: x**x, range(1,11))))

#reduce - single result
print('######### reduce #######')
number = [2,1,6,4]
print(reduce(lambda x,y : x+y, number)) # add the first 2, then add result with 3 rd element and so on
print(reduce(lambda x,y : x*y, number))
print(reduce(lambda x,y : max(x,y), number))
print(reduce(lambda x,y : min(x,y), number))

print(reduce(lambda x,y : x if len(x) > len(y) else y, words))

#exercise - take a list - filter odd numbers, sqaure it and sum it

sample = [1,4,5,6,7,8,9]
print(list(map( lambda x: x*x, filter(lambda x: x%2, sample)))) #square
print(sum(list(map( lambda x: x*x, filter(lambda x: x%2, sample)))))

print(reduce (lambda x,y: x+y, (map( lambda x: x*x, filter(lambda x: x%2, sample)))))

#exercise
months = [('Jan', 31), ('Feb',28), ('Mar',31)]

t = ('Jan',31)
print(t[0])
print(t[1])

print(sum(map(lambda x: x[1], months))) #sum of the days

print(reduce(lambda x,y : x if x[1] < y[1] else y, months)) #leaset no of days
print(reduce(lambda x,y : x if x[1] < y[1] else y, months)[0]) #returns month with least days
