
# a = 10 
# b = 20 

# if a > b:
#     print("a is greater")
# else:
#     print("b is greater")


# QUestion : write a function to check which number is greater among two numbers .

# function defition :

# def check_greater_number(a,b):

#                     if a > b:
#                         print("a is greater" , a)
#                     else:
#                         print("b is greater" , b)

# # function call :
# check_greater_number(100,200)  

# check_greater_number => this is function name 
# def => keyword to define a function 
# (a, b ) => parameters 





# def find_square():
#     my_variable = int(input("HIi, Wilmot please enter any number to find sqr: "))
#     print("hii WImot here is your sqr: ",my_variable * my_variable)

# find_square()

# Task: write a function to print the cube of a number.


# cube of 4 => 4 * 4 * 4 = 64

# my_number = 4
# print("The cube of my_number is : ", my_number * my_number * my_number)


# def print_cube_function(my_number):
#           print("The cube of my_number is : ", my_number * my_number * my_number)

# # function call
# print_cube_function(4)  ## 64



## even number => divisible by 2
## odd number => not divisible by 2

# modulus operator => %
# => it gives the remainder after division

# 12 % 2 => 0  => even number
# ----------------------------------------------- 
# a = 15

# if a % 2 == 0:
#     print("a is even number")
# else:
#     print("a is odd number")




# def check_even_odd(x):
   
#     if x % 2 == 0:
#              print("this is even number ")
#     else:
#              print("this is odd number ")


# # function call
# check_even_odd(10)  ## even number
# print("This is wilmot here")
# check_even_odd(7)   ## odd number


# for i in range (13, 131, 13):
#     print(i)


# starint point => 13
# end point => 131 exclded
# Gap => 13 , (N-1) ,13 - 1 => 12 , you have to skip 12 elements
# i => loop variable


# for i in range (13, 131, 13):
#     print(i)


def print_table_of_any_number(x):
    for i in range(x, x*10+1, x):
        print(i)
        
# function call
print_table_of_any_number(7)  ## table of 7