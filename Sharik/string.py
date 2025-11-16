## String : -
# => A sequence of characters/alphabets/letters


# Letters => Characters
# Sentence/Words => Group of characters/alphabets => String 

# Example : "wilmot","Sharik", "Hello World" , 'Python Programming' , """Welcome to Python""" , '''Python is fun'''

# Alphabets/Letters/Characters : a,b,c.......z , A,B,C....Z

## Words/Sentences : group of characters/alphabets


## Data Type : 

# Integer : 10,20,30,40
# Float : 10.5,20.5,30.5, 3.34,6.67
# Boolean : True, False
# String : "Hello", 'Python', """Welcome to Python""", '''Python is fun'''

# int i = 5;

# What is Data Type?
# => Data Type is a classification that specifies which type of value a variable can hold .

my_name = "Sharik"
print(my_name)
print(type(my_name))  


# String : A sequence of characters/alphabets/letters

## String Operations : -
# => 1. Concatenation ("+") : Joining two or more strings together

first_name = "Sharik"
last_name = "Ahmed"
full_name = first_name + " " + last_name
print(full_name)  # Output: Sharik Ahmed

## 2. Replication ("*") : Repeating a string multiple times

my_namee = "WIlmot"
print(my_namee * 10)  # Output: WIlmotWIlmotWIlmot


# ctrl + f => search any word in the file 
# if we want to replace his_name to my_name in entire file



print("PHP")

## Task => instead of Java i just want to print Javascript in all files 

## SOme methods in string :
# 1. len() => it is used to find the length of string
# 2. lower() => it is used to convert the string to lowercase
# 3. upper() => it is used to convert the string to uppercase
# 4. title() => it is used to convert the first character of each word to uppercase
# 5. strip() => it is used to remove the leading and trailing whitespace from the string
# 6. replace() => it is used to replace a substring with another substring
# 7. split() => it is used to split the string into a list of substrings based
# 8. join() => it is used to join a list of strings into a single string with a specified separator


# 9. find() => it is used to find the index of the first occurrence of a substring

# 10. count() => it is used to count the number of occurrences of a substring in the string
# 14. startswith() => it is used to check if the string starts with a specified substring
# 15. endswith() => it is used to check if the string ends with a specified substring
# # 16. index() => it is used to find the index of the first occurrence of a substring (raises an error if not found)

# 17. capitalize() => it is used to convert the first character of the string to uppercase and the rest to lowercase

# W$i$l$m$o$T
std_name = "Wilmot"
sentence = "        Welcome to python programming"
print(std_name)
print(len(std_name))  # 6
print("the output of lower is : ", std_name.lower())  # wilmot
print("the output of upper is : ", std_name.upper())  # WILMOT
print("our main sentence is : ", sentence)  # Welcome to python 
print("the output of title is : ", sentence.title())  # Welcome 
print("the output of strip is : ", sentence.strip())  # Welcome to python programming
print("output of replace is : ", sentence.replace("python", "Java"))
print("output of split is : ", sentence.split())  # ['Welcome', 'to', 'python', 'programming']

# List = ['Wilmot', 'Sharik', 'Pandey']
print("output of join is : ", "--".join(std_name))  # W$i$l$m$o$t

# Seperator => "--"

my_string = "Programming"
print("the output of find is : ", my_string.find("g"))  # 3
print("the output of count is : ", my_string.count("g"))  # 3
print("the output of startswith is : ", my_string.startswith("W"))

print("the output of endswith is : ", my_string.endswith("g"))

print("the output of index is : ", my_string.index("g"))  


my_sentence = "wilmot is a nice guy"
print("the output of capitalize is : ", my_sentence.capitalize())

