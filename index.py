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
# fruit.add('papaya')
# fruit.update({'watermelon', 'pawpaw'})
# # fruit.remove('mango')
# fruit.discard('mango')
# fruit.pop()
# fruit.clear()
# print(fruit)


# fruits = {'apple', 'orange', 'grape'}
# vowels = set('fruits')
# print("u" in vowels)


#set operations
# set1 = {1, 2, 3}
# set2 = {3,4,5}

# #union of the set
# union_set = set1 | set2
# print(union_set)


# #intersection of the set
# intersection_set = set1 & set2
# print(intersection_set)

# #difference of the set
# difference_set = set1 - set2
# print(difference_set)


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


#dictionary
#it is an unordered collection of data value. It is always in key and value.
# car = {
#     "brand" : "Toyota",
#     "year": 2015
# }

# #using the get method
# print(car.get('year'))

# #the indexing method
# print(car['brand'])

#modifying a dictionary

# car['brand'] = 'Benz'
# car['color' ] = 'Blue'
# print(car)


#nested dictionaries
# studentsMarks = {
#     "Ola": {
#         'Maths': 70,
#         "English": 80,
#     },
#     "Shola":{
#         "Maths": 74,
#         "English": 50
#     }
# }

# print(studentsMarks)
# print(studentsMarks.get('Ola'))

#adding key and value to a nested dictionary
# studentsMarks['Shade'] = {}
# studentsMarks['Shade']['Maths'] = 80
# studentsMarks['Shade']['English'] = 90

# # print(studentsMarks['Shade'])

#how to remove element of a dictionary
# studentsMarks.pop('Ola')
# print(studentsMarks)


#stacks and queues

letters = []
# letters.append('a')
# letters.append('b')
# letters.append('c')
# letters.append('d')


# letters.pop()
# print(letters)


#stack using the deque library
# Dequeue is a short form of double ended queue

# from collections import deque
# numbers = deque()

# numbers.append(23)
# numbers.append(24)
# numbers.append(50)

# numbers.pop()
# print(numbers)


#queues using the deque library

# from collections import deque
# names = deque()
# names.append('Taiwo')
# names.append('Kehinde')
# names.append('Ola')

# names.popleft()
# print(names)

#space and time complexity


#constant time complexity
# def firstElement(listSample):
#     print(listSample[0])


# firstElement([1, 2, 3, 4, 5]) # 0(1)

#linear time complexity
# using the for-in loop

# def firstElement(listSample):
#     for item in listSample:
#         print(item * 2)
    
# firstElement([1, 2, 3, 4, 5])  # 0(n)

# x = 3

# if(x == 0):
#     print(x, " is equal to zero")
# elif(x == 1):
#     print(x, " is equal to one")
# elif(x > 2): 
#     print(x, " is greater than two")
# else: 
#     print(x, " is not equal to zero")


    #write a code that analyzes the performances of students in the department of Software Engineering. The total marks for Javascript is 100marks, the pass mark is 50marks, the excellent mark is 80marks. Prompt for their mark and tell them their results.


#loop
# a = [2, 3, 4, 5, 6]


# #for loop syntax

# for i in a:
#     print(i * 2)


# number = [2, 6, 5, 8, 3]

# for i in number:
#     if(i % 2  != 0):   #if(i % 2 != 0)
#         print(i, "not divisible by 2") 


        #assignment
        #1. given a list with elements, return  the  largest element in the list.

#Test data: const arrayNumber = [20, 21, 18, 15, 10, 9, 8, 7, 45]

#2. using python function write a program that returns the multiples of 3 and 5 between 0 and 100;


#3
#Mark and John are trying to compare their BMI(body mass index) which is calculated using the formula  BMI = mass/h2(height * height).
#1. store Mark's and John's mass and height in variables.
#2. calculate both their BMIs using the formula.
#3. write a code that check if Mark's BMI is greater than John's BMI using python function.

#TEST DATA
#1. Marks mass 78kg, height is 1.69m tall
#Johns mass 92kg, height is 1.95m tall

#2. Marks mass 95kg, height is 1.88m tall
#Johns mass 85kg, height is 1.76m tall


#while loop

# x = 1
# while x <= 5:
#     print (x)
#     x = x + 1

# else:
#     print (x, "is no longer less than 5")

#function in python
#in-built functions in python
# abs(11)
# abs(-12)

# x = dict(sur_name='Ola', age= 15)
# print(x)

# name = input("Input name:")


# def addNumbers():
#     a = 2
#     b = 3
#     print(a + b)
# addNumbers()


#parameters, arguments;

# def showParameter(a, b, c):  #parameters
#     print(a + b + c)
# showParameter(1, 2, 3) #arguments


# def getNumber(a):
#     for i in a:
#      print(i * 2)
# getNumber([2,3,4,5,6])

# def checkCondition(x):
#     if(x > 10):
#         print(x, ": greater than 10")
#     else:
#         print(x, ": less than 10")
# checkCondition(50)

#OOP object oriented programming

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
# p1 = Person("Bola", 25)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def showClassName(self):
#         print(self.name)
# # p1 = Person("Bola", 25)
# # p1.display()


# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)

# s1 = Student("Shola", 15)
# # print(s1.name)
# s1.showClassName()
# p1.name = "Shade"
# print(p1.name)
# print(p1.age)

import pandas as pd

#load csv in python....
employeeData = pd.read_csv('employee.csv')


# print(employeeData.select_dtypes("object"))
print(employeeData["MonthlyIncome"].max())
print(employeeData["MonthlyIncome"].min())
print(employeeData["MonthlyIncome"].mean())

























