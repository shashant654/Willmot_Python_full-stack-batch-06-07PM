# # name , age , department, and data are keys
# => Sharik, 19 , Cse , 1111111 => these are values
my_dict = {
                    "name": "Sharik",
                    "age" : 19,
                    "department": "CSE",
                    "data" : "11111111111"
}

print(my_dict["name"])  # Sharik
print("using get method => ", my_dict.get("name")) # Sharik
print("get all keys", my_dict.keys())
print("get all values: ", my_dict.values())

print("using items method=> ", my_dict.items())

my_dict["data"]  = "this is my data"
print("after changing the value of data key=> ", my_dict )

my_dict.update({"roll": "111"})
print("after applying update method => ", my_dict)

my_dict.update({"roll" : "222"})
print("after changing the roll using update method ", my_dict)

# my_dict.pop() # it gives error
# print("after applying pop method without any key ", my_dict)

my_dict.pop("department")
print("after applying pop method with any key ", my_dict)

my_new_dict = { "name" : "WIlmot", "roll": 1}

my_new_dict.popitem()

print("my_new_dictionary looks like this ", my_new_dict)

my_new_dict.clear()

print("after applying clear method ", my_new_dict)


# 1. get() => it returns the values for a specified key.
# 2. keys()  => it returns all keys of any object.
# 3. values() => it returns all values of any object.
# 4. items()  => it returns key-value pairs

# 5. update() => you can add one more new field or you can update any existed field .

# 6. pop()  => using this method we can remove any data from a list.
# Note:  pop expected at least 1 argument

# => pop("name")

# 7. popitem() => it can remove last key pair value.

# 8. clear() => by using this method , we can remove entire element from a dictionary.

# in Python , we say Dictionary
# in c and C++ , we say it map ( ordered map and unordered map)
# in javascript , we say it objects 