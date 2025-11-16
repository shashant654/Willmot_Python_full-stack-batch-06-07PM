# # set :-

# => it's a collection of unique elements.
# => it can't contain duplicate elements.
# => it is similar to list but only one difference is it can not contain duplicate element 
# => it is also mutable.
# => it is unordered (elements have no fixed position),

# # EX: { 22,34,55,66,77,88 }

# # tuple : (22,33,44,55,)
# # list : [ 33,44,55,66,77]

# #   0  1  2  3   4  5   6  7
# # { 22,34,55,66,77,88, 55, 55 }

# # my_set = { 22,34,55,66,77,88, 55, 55 }
# # print("this set looks like this : ",my_set)
# # print("the value of 3rd index: ", my_set[3]) # error


# # You tried to access an element by index (like my_set[3]),
# # but sets in Python do not support indexing.

# #  0  1  2  3  4  5  6   7   8    9
# # 22,34,55,66,77,88, 55, 55, 110, 200

# # my_set = { 22,34,55,66,77,88, 55, 55, 110, 200 }
# # print(my_set)  

# # print(my_set[9])  
# # => it gives error , because it's indexing will be unbalanced , after removing the duplicate elements



# # my_set = { 22,34,55,66,77,88, 110, 200 }
# # print(my_set)  
# # my_set.add(202)

# # print("my new set looks like this : ", my_set)

# # 1. add() => using this method , we can add any element at any random index.
# # => add() takes exactly one argument



# # my_set = { 22,34,55,66,77,88, 110, 200 }
# # print(my_set)  
# # my_set.add(202,403, 404) # it gives error becaue add() can add  only one element 

# # print("my new set looks like this : ", my_set)

# # 2. update() => 



# # my_set = { 22,34,55,66,77,88, 110, 200 }
# # print(my_set)  
# # my_set.update([222,333,555])


# # print("my new set looks like this : ", my_set)
# # my_set.update([222,555, 999])
# # print("my new version of set looks like this : ", my_set)

# # nOte: Dictionary is ordered data structure.

# # 3. remove() :-
# # => it removes a specific element from any set , and if that specific element does not exist , it gives error.



# # my_set = { 22,34,55,66,77,88, 110, 200 }
# # print(my_set)  
# # my_set.remove(22)
# # print("my new set looks like this : ", my_set)
# # my_set.remove(111) # error : because 111 does not exist in set.
# # print(my_set)


# # discard() :-
# # => by using this method , we can discard any specific eleement , and if that element does not exist then it just ignore ,and does not give any error.

# # my_set = { 22,34,55,66,77,88, 110, 200 }
# # print(my_set)  
# # my_set.discard(22)
# # print("my new set looks like this : ", my_set)
# # my_set.discard(111) 
# # print(my_set)

# # # pop():-
# # # =>  it removes any random element.
# # => pop() takes no arguments 

# # my_set = { 22,34,55,66,77,88, 110, 200 }
# # print(my_set)  
# # my_set.pop()  # it removes any random element.
# # print("my new set looks like this : ", my_set)
# # my_set.pop(55) # error: set.pop() takes no arguments 
# # print(my_set)


# # my_set = { 22,34,55,66,77,88, 110, 200 }
# # print(my_set)  
# # my_set.clear()  
# # print("my new set looks like this : ", my_set)

# # union() => 


# # Sharik_set = { 22, 40, 44}
# # Wilmot_set = { 33, 22}
# # print( "the union of this both set is :", Sharik_set.union(Wilmot_set))



# # # UNION :-

# # Sharik_set = { 22, 40, 44}
# # Wilmot_set = { 33, 22}

# # Sharik_set U Wilmot_set  => 22, 40, 44, 33
# # # result = similar element in both set and rest of elemets 

# # intersection() :-


# # => it returns only those elements that are eixisted in both set . 


Sharik_set = { 22, 40, 44}
Wilmot_set = { 33, 22}
print( "the intersection of this both set is :", Sharik_set.intersection(Wilmot_set))