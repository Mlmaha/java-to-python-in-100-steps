#lists
marks = [10,20,25]
print(marks)

#insert
marks.insert(1,22) #index position & number
print(marks)

marks.append(30) #insert at the last
print(marks)

print(sum(marks))
print(min(marks))
print(max(marks))
print(len(marks))

marks.remove(25) #removes the element 20
del marks[0] #removes the element at index 1

print(marks)
print(55 in marks) #false - checks the element in array

print(marks.index(22))

for i in marks:
    print(i)

######################
list1 = ['maha', 'hello']
list1.extend('maha') #splits into char's and append at the end
print(list1)

#list.extend(['saraa','meena']) - not working, need to check
list1 = list1+ ['saraa','meena']
print(list1)

#################

#slicing
print('slicing')
list2 = ['one','two','three','four','five','six']
print(list2[2:5])
print(list2[:3])
print(list2[:])
print(list2[2:])

print(list2[1:5:2]) #every 2 nd element
print(list2[::2]) #every 2 nd element
print(list2[::-2]) #from right side - reverse

del list2[:1]
#list2[2:5] = [3,4,5]
print(list2)

##############
print('############ reverse')
list2.reverse() #reverses the original list
print(list2)
print(reversed(list2)) #to access the list in a reverse way, no chnage in original list
for number in reversed(list2):
    print(number)

print('######### sorting')
list2.sort() ##sorts the original list
print(list2)
for number in sorted(list2): ##to access the list in a sorted order,  no chnage in original list
    print(number)

list2 = ['one','two','three','four','five','six']
list2.sort(key=len, reverse=True)
print(list2)
for number in sorted(list2,key=len, reverse=True): #key=len - how we want to sort
    print(number)

#############
#list as stack - LIFO
number = []
number.append(5)
number.append(2)
number.append(8)
number.pop() #deletes last element
print(number)

#list as queue - FIFO
number = []
number.append(5)
number.append(2)
number.append(8)
number.pop(0) ##deletes element at 0 index
print(number)

###############
list2 = ['one','two','three','four','five','six']
number_with_length_four = []
for number in list2:
    if(len(number) == 4):
        number_with_length_four.append(number)

#list comprehension
number_with_length_four = [number.upper() for number in list2]
print(number_with_length_four)

#alternate way - for the above logic
number_with_length_four = [number.upper() for number in list2 if len(number)==4]
print(number_with_length_four)

###############
#set - no duplicates
print('############## set')
number = [1,2,1,3,2]
sample = set(number) #removes duplicates from list
print(sample)

sample.add(3) #no effect
sample.add(1) #no effect

sample.add(4)
sample.remove(4)
print(sample)

min(sample)
max(sample)
len(sample)
#sample[0] - index is not allowed in set

set_1to5 = set(range(1,6))
set_1to10 = set(range(1,10))
#union of 2 sets
print(set_1to5 | set_1to10) #combines both
print(set_1to5 & set_1to10) #intersect - print common elements
print(set_1to5 - set_1to10) #prints elements from first set which are not in second set

######################
#dictionary
sample_dictionary = dict(a=2, b=5, c=8)
print(sample_dictionary)

sample_dictionary['d'] = 10
print(sample_dictionary)

print(sample_dictionary['d'])

print(sample_dictionary.get('c'))

sample_dictionary.keys() #returns key
sample_dictionary.values() ##returns value
sample_dictionary.items() #returns both key & value

for key,value in sample_dictionary.items():
    print(f'key: {key} ,value: {value}')

del sample_dictionary['a']

##############################

square_list = [number*number for number in range(1,11)]
square_set = {number*number for number in range(1,11)}
square_dict = {number:number*number for number in range(1,11)}
print(type(square_list))
print(type(square_set))
print(type(square_dict))

print(square_list)
print(square_set)
print(square_dict)

#################################
#tuple - immutable, spectfic attributes related to each other, not number of elements
person = ('Maha', 5, 'India')
print(type(person))
person2 = ('sarra', 10, 'India') #used to store multiple values
print(type(person2))

x,y = 0,1
print(x,y)
x,y = y,x
print(x,y)

def getperson():
    return 'Maha', 5, 'India'

person = getperson()
print(type(person))

