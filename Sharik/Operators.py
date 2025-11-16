
# Operators: +, -, *, /, %, //, **

# + => Addition
# - => Subtraction
# * => Multiplication
# / => Division
# % => Modulus
# // => Floor Division
# ** => Exponentiation

# 3**6 => 3^6 => 3*3*3*3*3*3 => 729

a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333333333333335
print(a // b)  # 3
print(a % b)  # 1

print(a ** 3)
# 10 * 10 * 10 = 1000


# Assignment Operators: =, +=, -=, *=, /=, %=, //=, **=

x = 20
y = 5
# x += y  
x = x + y 
print(x)

# the task is we wanna add in x => both  X and Y 
# x = x + y => it takes more time to run 
# x += y  => it takes less time to run 
# print(x + y) 

# in future we will learn about Time complexity, Space complexity

# # 3. Comparison Operators: ==, !=, >, <, >=, <=
# ------------------------ 
# => in this case we will get the output in boolean format => True, False

p = 10
q = 20
C = 20
print(p == q)  
print(p == C)
print(p != q)
print(p > q)
print("Hii Wilmot plzz confirm this stmt: ",p < q)
print("hello Wilmot plzz confirm this stmt: ",p >= q)

print("Hello SHarky plzz confirm this stmt: ",C <= q)


# 4. Logical Operators: and, or, not

# and => both the conditions should be true
# or => any one condition should be true
# not => negates the condition


# and operator => it gives True if both  conditions are True otherwise it gives False.
u = 10
v = 20
print(u < v and  u > v)
# True and False => False

# or operator => it gives True if any one condition is True otherwise it gives False.

s = 10
t = 20
print(s < t or s > t)
# True or False => True

## not operator => it negates the condition
m = 10
n = 20
print(not(m < n))
# not(True) => False
# not(False) => True
print(not(m > n))

# 6. Bitwise Operators: &, |, ^, ~, <<, >>


# & =>  Bitwise AND
# | =>  Bitwise OR           
# ^ =>  Bitwise XOR
# ~ =>  Bitwise NOT






e = 10
f = 2 
# or operator => it gives True if any one condition is True otherwise it gives False.
print("the result of e & f is: ", e & f)  # 2
print("the result of e | f is: ", e | f)  # 10
# print("the result of ~e is: ", ~e)  # -11
print("the result of e ^ f is: ", e ^ f)  # 8

# the binary of 10 => 1010
# the binary of 2 => 0010

# Notes: we can consider 1 => True and 0 => False




## Membership Operators : in, not in
# in => it returns True if the value is present in the sequence otherwise it returns False

# not in => it returns True if the value is not present in the sequence otherwise it returns False

# list is similar to arrary in other programming languages

# Question : check 10 is present in the list1 or not ?
list1 = [10, 20, 30, 40, 50]
print(" 10 in list1: ", 10 in list1)  # True
print(" 100 in list1: ", 100 in list1)  # False
print(" 100 not in list1: ", 100 not in list1)  # True


# Indentation => it is used to define a block of code in python
# => backbone of python programming language



print("PHP")