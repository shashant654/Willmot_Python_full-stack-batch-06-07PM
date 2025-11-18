# function:-

# 1. function definition 
# 2. function call

# 1. what is function definition?
# => a function definition is where you create a function.

# Example:-
# def my_function_name():
#                     print("thias is my function")

# 2. what is function call?
# => a function call is when you use a function after define it.


# def my_function_name():
#                     print("thias is my function")




# my_function_name()  # function call
 

 

# my_function_name()   ## this is my function



# def my_function_name():
#                     print("thias is my function")



# there are 2 types of function in python:

# 1. in-built function OR pre-defined function
# 2. user-defined function

# #### in-built function OR pre-defined function => no need to define it , we can directly use it.
# Example: print(), input(), len(), type() etc.


# print("suhani")

# print(sum([1,2,3,4,5])) ## 15 , sum is in-built function

# # this is user defined function 
# def sharik_function():
#     print("this is sharik function")


# sharik_function()  # function call



# print(max([1,9992,23,40,55]))  ## 9992 , max is in-built function
# print(len("suhani"))  ## 6 , len is in-built function
# print(min([1,2,3,4,5]))  ## 1 , min is in-built function


# 8 => integer
# 8.9 => float
# "suhani" => string
# True/False => boolean
#  type(), max(), min()  ## pre-defined function
# print(type(8))  ## <class 'int'>  # pre-defined function
# print(type(8.9))  ## <class 'float'>  # pre-defined function
# print(type("suhani"))  ## <class 'str'>  # pre-defined function
# print(type(True))  ## <class 'bool'>  # pre-defined function



# print( ), input(), len(),


# 2. user-defined function => we have to define it firstly, then we can use it.


# def my_function():
#                     my_name = "Wilmot"
#                     print(my_name*5)

# my_function()  # function call

# string replication (*) operator

#####   the task is i have to add two elements

# a = 10
# b = 20
# print("The sum of a and b is : ", a + b)  ## 30



# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("The sum of a and b is : ", a + b)  ## 30




# def add_two_numbers(a,b):
#     print("The sum of a and b is : ", a + b)


# add_two_numbers(10,20)  ## 30
# print("Hii, wilmot here, how are you?")

# add_two_numbers(100,200)  ## 300
# print("This is sharik here, good morning!")

# add_two_numbers(50,15)  ## 65


# 2. task :- write a function to add three numbers and print their sum.

# def add_three_numbers(x,y,z):
#     print("The sum of x, y and z is : ", x + y + z)


# print("hii, wilmot here, i have created a function to add three numbers.")

# add_three_numbers(10,20,30)  ## 60


# 3. task :- write a function to print the square of a number.

def my_print_square_function(my_number):
                    print("The square of my_number is : ", my_number * my_number)

my_print_square_function(5)  ## 25