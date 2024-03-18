# print('Hello world')
name = 'Shade' #str data type
x = '2'

y = 3 # int data type

z = 3.4 # float data type
# print(type(z))

fruits = ['apple', 'orange', 'pawpaw', 'pineapple'] # list data type

# print(type(fruits))

#int()  float() str()



#type casting
#type casting means converting one data type to another
# you can use an int function to convert a float or string data type to an integer type
# x = int(x)
# z= int(z)
# print(type(x))
# print(type(z))

# x = float(x)
# print(type(x))


# z = float(z)
# print(type(z))

# x = str(x)
# print(type(x))

# z = str(z)
# print(type(z))

# y = ("apple", "orange", "mango") #tuple data type.
# print(type(y))


#example of a local variable.
def func():
    a = 2
    b = 3
    c = a + b
    # print(c)

func()

# print(a)


#example of a global variable
a = '5'

def func():
    b = '10'
    c = a + b
    # print(c)
func()


#list methods
# fruit = ['apple', 'orange', 'pineapple', 'papaya']
# #append method
# fruit.append('mango')
# fruit.insert(0, 'watermelon')
# fruit.remove('apple')
# fruit.pop()
# fruit.sort()
# print(len(fruit))
# print(fruit)


#tuples
fruit = ('apple', 'watermelon')

#Accessing the tuple elements
# print(fruit[1])


#concatenation operations in tuple;
fruit = ('apple', 'watermelon', "pineapple")
veg = ('tomato', 'potato', 'onion')
combined_fruits = fruit + veg 
# print(combined_fruits)


#repetition operations in tuple
repeated_fruits = fruit * 3
# print(repeated_fruits)


#slicing operations in tuple
sliced_fruits = fruit[2:]
# print(sliced_fruits)

#set 
fruit = {'apple', 'orange'}
vowels = set('aeiou')
# print('a' in vowels)
# print('y' in vowels)
# print(type(vowels))

#set method
#add
fruit.add('papaya')
fruit.update({'watermelon', 'pawpaw'})
# fruit.remove('mango')
fruit.discard('mango')
fruit.pop()
fruit.clear()
print(fruit)


# fruits = {'apple', 'orange', 'grape'}
# vowels = set('fruits')
# print("u" in vowels)

# from collections import deque

# numbers = deque()
# numbers.append(23)
# numbers.append(24)
# numbers.append(50)

# numbers.pop()
# print(numbers)


# def firstElement(listSample):
#     print(listSample[0])


# import timeit

# def firstElement(listSample):
#     print(listSample[0])

# # Measure the execution time
# execution_time = timeit.timeit('firstElement([1, 2, 3, 4, 5])', globals=globals(), number=1000)
# print(f"Execution time: {execution_time}")






