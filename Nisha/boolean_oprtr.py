#  Bitwise Operators:

# => &, |, ^, ~
 
 # 1. and ("&") => it gives ("1") if both conditions are ("1")
# otherwise it gives ("0")

# 2. or ("|") => it gives ("0") if both conditions are ("0")
# otherwise it gives ("1")

# 3. not ("!") => it gives True ("1") if the condition is False ("0")
# # otherwise it gives False ("0")


a = 10  # binary number of 10 => 1010
b = 5   # binary number of 5  => 0101
print("the output of a & b is :", a & b)  
print("the output of a | b is :", a | b)


#    4 4 5 2
# +  3 2 1 0 
# -----------
#    7 6 6 2


#    1 0 1 0
#  & 0 1 0 1


# 1. 0 & 1 => 0
# 2. 1 & 0 => 0
# 3. 0 & 0 => 0
# 4. 1 & 0 => 0

# output => 0 0 0 0 => 0

#     1 0 1 0
#   | 0 1 0 1
#   -----------



# 1. 0 | 1 => 1
# 2. 1 | 0 => 1
# 3. 0 | 1 => 1
# 4. 1 | 0 => 1

# output => 1 1 1 1 => 15


# Bitwise XOR (^): 
# => it gives ("1") if both conditions are different          
# => otherwise it gives ("0")

a = 13
b = 2 

print("the output of a ^ b is :", a ^ b)

# Bitwiswe NOT (~):
# => it gives the one's complement of the number

a = 10
print("the output of ~a is :", ~a)  # - ( n + 1)